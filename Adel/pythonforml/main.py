import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error


# Load the diabetes dataset

# dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])


diabetes = datasets.load_diabetes()
diabetes_X = diabetes.data
# Use only one feature to tarin the model
diabetes_X_train = diabetes_X[:-30]
# Use only one feature to test the model
diabetes_X_test = diabetes_X[-30:]
# Use only one labels to train the model
diabetes_y_train = diabetes.target[:-30]
# Use only one labels to test the model
diabetes_y_test = diabetes.target[-30:]

# Create linear regression object
model=linear_model.LinearRegression()
# Train the model using the training sets
model.fit(diabetes_X_train, diabetes_y_train)
# The coefficients
diabetes_y_test_pred = model.predict(diabetes_X_test)

print("Mean squared error is: ", mean_squared_error(diabetes_y_test, diabetes_y_test_pred))
print("Weights: ", model.coef_)
print("Intercept: ", model.intercept_)




