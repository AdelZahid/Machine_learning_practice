def fn(x):
    return x**2 - 4*x -10

indx=True

while indx:
    x1=int(input("Enter the value of x1: "))
    x2=int(input("Enter the value of x2: "))
    if fn(x1)*fn(x2)<0:
        indx=False
        break
    else:
        print("incorrect range:")
        


c=(x1+x2)/2
err=0.00001
while abs(fn(c))<=err:
        if fn(x1)*fn(c)<0:
            x2=c
        else:
            x1=c
        c=(x1+x2)/2
print(c)