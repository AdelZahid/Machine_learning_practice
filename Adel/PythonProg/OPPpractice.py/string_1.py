str=input("input the string 1:")
len1=len(str)
str2=input("input the String two:")
len2=len(str2)
print(len1)
print(len2)
str3=str+" "+str2

#slicing of the string

print(str3[1:5])
print(str3[3:]) #from third index to last
print(str3[:6]) #form first to six index

# functions
print(str3.replace(str2," Lossers"))
print(str3.capitalize())
print(str3.find("ld"))
print(str3.find("hellow"))
print(str3.count("W"))