T=1
while T<=100:
    print(T)
    T+=1

num=[1,4,3,6,7,3,5,67,5,4,55]
# i=0
n=len(num)-1
# while i!=n:
#     print(num[i])
#     i+=1

x = int(input("Enter the number: "))  
j = 0

while j != n:
    if num[j] == x:
        print("Found the number at position: ", j)
        break  
    j += 1

else:
    print("Number not found")


for el in num:
    print(el)
    

for el in num:
    if el==x:
        print("Found the number")
        break

else:
    print("Number not found")
    
#range in loop

for ele in range(2,12,2):
    print(ele)

#print table of n for term of z

n=int(input("Enter the number: "))
z=int(input("Enter the limit: "))

for i in range(z):
    print(n*i)
    
    
n1=int(input("Enter the number: "))
sum=0
i=0
while i<=n1:
    sum+=i
    i+=1

print("Sum of the numbers is: ",sum)

#find factorial

n=int(input("Enter the number: "))

i=1
fact=1
while i<=n:
    for el in range(1,i+1):
        fact*=el
    print("The factorial of ",i ,"is :",fact)
    fact=1
    i+=1
