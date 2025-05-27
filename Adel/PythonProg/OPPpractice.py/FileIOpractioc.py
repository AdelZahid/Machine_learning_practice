

str1=input(str("Enter the sentence: "))
str2=input(str("Enter the sentence: "))
str3=input(str("Enter the sentence: "))
str4=input(str("Enter the sentence: "))

with open("Practice.txt","w") as fl:
    fl.write(str1+"\n"+str2+"\n"+str3+"\n"+str4+"\n")
    fl.close()

with open("Practice.txt","r") as fl:
    data=fl.read()
new_data=data.replace("Fuck","suck")
fl.close()


with open("Practice.txt","w") as fl:
    fl.write(new_data)
    fl.close()
    
def find_inline(line):
    issearch=True
    isnotFound=True
    ln_no=1
    with open("Practice.txt","r") as fl:
        while issearch:
            data=fl.readline()
            if(line in data):
                print(f"Found '{line}' in line {ln_no}")
                ln_no+=1
                isnotFound=False
            else:
                if(data==""):
                    issearch=False
        if(isnotFound):
            print("Dosent found:")
word=input(str("enter the word for search: "))
find_inline(word)
fl.close()

n = int(input("Input the range: "))
elem = []

for _ in range(n):
    elem.append(input("Enter the number: "))

with open("Practice.txt", "a") as fl:
    fl.write(", ".join(elem))  # Writing the elements as a comma-separated string

with open("Practice.txt", "r") as fl:
    data = fl.read()

# Function to find odd numbers in the string
def find_odd(string):
    for char in string:
        if char.isdigit():  # Ensure that the character is a digit
            if int(char) % 2 != 0:
                print(f"Odd number is {char}")
find_odd(data)
