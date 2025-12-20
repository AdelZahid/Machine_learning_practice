# fake_news_app.py
from flask import Flask, render_template, request, jsonify
import pickle
import re
import numpy as np
import requests
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import nltk
import urllib.parse
import time

app = Flask(__name__)

# Download NLTK data if not already downloaded
try:
    nltk.data.find('corpora/stopwords')
    nltk.data.find('corpora/wordnet')
except:
    nltk.download('stopwords')
    nltk.download('wordnet')

# Load your trained model
try:
    with open('fake_news_model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("✓ Model loaded successfully!")
except Exception as e:
    print(f"✗ Error loading model: {e}")
    model = None

# Initialize stemmer and lemmatizer
port_stem = PorterStemmer()
word_lem = WordNetLemmatizer()

def transform_text(text):
    """Your text preprocessing function"""
    text = str(text).lower()
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.split()
    text = [port_stem.stem(word) for word in text if word not in stopwords.words('english')]
    text = ' '.join(text)
    return text

def extract_news_from_url(url):
    """Extract news content from URL"""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Extract title
        title = soup.find('title')
        title_text = title.get_text() if title else 'Unknown Title'
        
        # Extract author (common patterns)
        author = 'Unknown Author'
        author_tags = soup.find_all(['span', 'div', 'p'], class_=re.compile(r'author|byline|writer', re.I))
        for tag in author_tags:
            text = tag.get_text(strip=True)
            if text and len(text) > 3:
                author = text
                break
        
        # Extract main content
        content = ''
        # Try common article selectors
        selectors = [
            'article', 
            '.article-content',
            '.story-content',
            '.post-content',
            '[class*="content"]',
            '[class*="article"]',
            '[class*="story"]'
        ]
        
        for selector in selectors:
            elements = soup.select(selector)
            for element in elements:
                paragraphs = element.find_all('p')
                if paragraphs:
                    content = ' '.join([p.get_text(strip=True) for p in paragraphs])
                    if len(content) > 100:
                        break
            if content:
                break
        
        # If no content found, get all paragraphs
        if not content or len(content) < 100:
            paragraphs = soup.find_all('p')
            content = ' '.join([p.get_text(strip=True) for p in paragraphs])
        
        return {
            'title': title_text,
            'author': author,
            'content': content[:1000],  # Limit content length
            'url': url,
            'success': True
        }
        
    except Exception as e:
        print(f"Error extracting from URL: {e}")
        return {
            'title': 'Error',
            'author': 'N/A',
            'content': '',
            'url': url,
            'success': False
        }

def predict_news(text):
    """Predict if news is fake or real"""
    if model is None:
        return None
    
    try:
        # Transform the text
        transformed_text = transform_text(text)
        
        # Load your vectorizer (you'll need to save this separately)
        try:
            with open('vectorizer.pkl', 'rb') as f:
                vectorizer = pickle.load(f)
            X_new = vectorizer.transform([transformed_text]).toarray()
        except:
            # If no saved vectorizer, you need to create/fit one
            print("Warning: Vectorizer not found")
            return None
        
        # Make prediction
        prediction = model.predict(X_new)[0]
        
        # Get prediction probability
        if hasattr(model, 'predict_proba'):
            probability = model.predict_proba(X_new)[0]
            confidence = max(probability) * 100
            real_prob = probability[0] if len(probability) > 1 else probability[0]
        else:
            confidence = 85.0  # Default confidence
            real_prob = 0.85 if prediction == 0 else 0.15
        
        return {
            'prediction': int(prediction),
            'is_fake': bool(prediction),
            'confidence': round(confidence, 2),
            'real_probability': round(real_prob * 100, 2),
            'text_sample': transformed_text[:200] + '...' if len(transformed_text) > 200 else transformed_text
        }
    except Exception as e:
        print(f"Error in prediction: {e}")
        return None

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_news():
    try:
        data = request.form
        url = data.get('url', '').strip()
        
        if not url:
            return jsonify({'error': 'Please provide a URL'})
        
        # Extract news from URL
        extracted_info = extract_news_from_url(url)
        
        if not extracted_info['success']:
            return jsonify({'error': 'Could not extract news from URL'})
        
        # Combine author and title for prediction (as per your training)
        text_for_prediction = extracted_info['author'] + ' ' + extracted_info['title']
        
        # Make prediction
        prediction_result = predict_news(text_for_prediction)
        
        if prediction_result is None:
            return jsonify({'error': 'Model prediction failed'})
        
        # Prepare response
        result = {
            'extraction_success': True,
            'extracted_info': {
                'title': extracted_info['title'],
                'author': extracted_info['author'],
                'content_preview': extracted_info['content'][:300] + '...' if len(extracted_info['content']) > 300 else extracted_info['content'],
                'url': extracted_info['url']
            },
            'prediction': {
                'is_fake': prediction_result['is_fake'],
                'status': 'FAKE NEWS ⚠️' if prediction_result['is_fake'] else 'REAL NEWS ✅',
                'confidence': prediction_result['confidence'],
                'authenticity_score': prediction_result['real_probability'],
                'explanation': 'This news appears to be fabricated or contains misleading information.' 
                               if prediction_result['is_fake'] 
                               else 'This news appears to be legitimate and fact-based.',
                'recommendation': '⚠️ Verify with other sources before sharing.' 
                               if prediction_result['is_fake'] 
                               else '✅ Source appears reliable.'
            }
        }
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'error': str(e)})

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint for direct text prediction"""
    try:
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({'error': 'No text provided'})
        
        text = data['text']
        prediction_result = predict_news(text)
        
        if prediction_result is None:
            return jsonify({'error': 'Prediction failed'})
        
        return jsonify({
            'text': text,
            'prediction': prediction_result['prediction'],
            'is_fake': prediction_result['is_fake'],
            'confidence': prediction_result['confidence'],
            'authenticity': prediction_result['real_probability']
        })
        
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)