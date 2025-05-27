
#all about conditional statements

light=input("The light colour: ")
if(light=="red"):
    print("stop")
elif(light=="Yellow"):
    print("slow down")
elif(light=="green"):
    print("go")
else:
    print("light is broken")
A=int(input("A: "))
G=input("M/F : ")
if(A<=100 and A>=80 and G=="M"):
    print("pass")
elif(A<=80 or A==33 and G=="F"):
    print("pass as consideration")
elif(A>33 and A<=44):
    print("Fail")
    
food=input("food: ")
eat="Yes" if food=="Cake" else "NO"
print(eat)
print("Sweet") if food=="Cake" or food=="Jalebi" else print("NO sweet")
age=int(input("age : "))
vote=("Yes", "No") [age<=18]
print(vote)








