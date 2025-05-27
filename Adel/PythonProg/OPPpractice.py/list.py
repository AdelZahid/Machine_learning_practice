#List

Student=["Adel",57,21,"Rampura"]
print(Student[0])
print(Student[1])
Student[0]="Alamin"
Student[1]=14
print(Student[0])
print(Student[1])

#list can be sliced too

marks=[55,66,77,88,99,100,111,112,113]
print(marks[2:5])
print(marks[:5])
print(marks[4:])

#methods in list

Marks2=[10,55,30,59,60,70,23,27,99]
Marks2.append(100)
print(Marks2)
print(Marks2.sort())
print(Marks2)
print(Marks2.sort(reverse=True))
print(Marks2)
print(Marks2.reverse())
print(Marks2)
Marks2.insert(4,304)
print(Marks2)

#ranging list can be used

print(list(range(11)))
