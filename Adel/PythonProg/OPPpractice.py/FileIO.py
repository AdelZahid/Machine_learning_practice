import os


# Writing to a file
with open("sample.txt", "w") as f:
    sant = input("Enter the sample text: ")
    f.write("I am back motherfuckers\n")
    f.write("Go suck your self\n")
    f.write(sant + "\n")

# Reading the file
with open("sample.txt", "r") as f:
    line = f.read()
    print(line)

# Reading line by line
with open("sample.txt", "r") as f:
    data = f.readline()
    print(data)
    data2 = f.readline()
    print(data2)



# Appending to file
with open("sample.txt", "a") as f:
    str1 = input("Enter your statement: ")
    f.write(str1 + "\n")


with open("sample.txt", "r") as f:
    line = f.read()
    print(line)
    
    
# Removing file
if os.path.exists("sample.txt"):
    os.remove("sample.txt")
    print("File removed successfully!")
else:
    print("File does not exist.")
