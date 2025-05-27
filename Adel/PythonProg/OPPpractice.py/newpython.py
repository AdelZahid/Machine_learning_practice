from collections import namedtuple


name= input("What is your name? ")
# Remove white space
name=name.strip()
#Capatilize fisrt letter of string
name=name.capitalize()
#capitalize all first after space


# name=name.title()
# print("hellow", name)
# x=int(input("What is the value of x?"))
# y=int(input("What is the value of y?"))
# print(x+y)
# sum=(float(input("Whats the value of Z: "))+float(input("Whats the value of R: ")))
# print(f"{round(sum):,}")
# div=(float(input("Whats the value of T: "))/float(input("Whats the value of N: ")))
# print(round(div,3))
# def hello(to="world"):
#     print(f"hello {to}")
# hello()
# hello(name)
# A,B=2,3
# C="@"
# print(A*C*B)
# a,b=1.5,3


#intiger division whiic works as a floor function

# print(a//b)


#power operator

# print(a**b)

#claver if

# sal=float(input("salary : "))
# tax= sal*(0.1,0.2) [sal<=50000]
# print(tax)

#oneline condition

# food=input("the name of item: ")
# print("Sweet") if food=="cake" or food=="Icecreame" else print("Not sweet")
# str=input("input the string 1:")
# len1=len(str)
# str2=input("input the String two:")
# len2=len(str2)
# print(len1)
# print(len2)
# str3=str+str2

#slicing of the string

# print(str3[1:5])
# print(str3[3:]) #from third index to last
# print(str3[:6]) #form first to six index

#replace function
# print(str3.replace(str2," Lossers"))


#List

# Student=["Adel",57,21,"Rampura"]
# print(Student[0])
# print(Student[1])
# Student[0]="Alamin"
# Student[1]=14
# print(Student[0])
# print(Student[1])

#list can be sliced too

# marks=[55,66,77,88,99,100,111,112,113]
# print(marks[2:5])
# print(marks[:5])
# print(marks[4:])

#methods in list

# Marks2=[10,55,30,59,60,70,23,27,99]
# print(Marks2.sort())
# print(Marks2)
# print(Marks2.sort(reverse=True))
# print(Marks2)
# print(Marks2.reverse())
# print(Marks2)
# Marks2.insert(4,304)
# print(Marks2)

#ranging list can be used

print(list(range(11)))

#name tuple

a=namedtuple('courses','name,technology')
s=a('datascience','python')
print(s)
s=a._make(['artificial intelligence','python'])
print(s)

#set 

collection={1,2,2,3,"hellow","world","hellow"}
print(collection)
print(len(collection))
collection.add("fuckyou")
print(collection)
collection.remove("world")
print(collection)
print(collection.pop())
print(collection)
collection.clear()
print(collection)

#functions of set

set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))
print(set1)
print(set2)
print(set1.intersection(set2))
