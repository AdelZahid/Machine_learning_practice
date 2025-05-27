#count factorial using function

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
n=int(input("enter the number: "))

for el in range(n+1):
    print("The factorial of ",el,"is: ",factorial(el))
    
#sum of natural number to n

def sum_natural(sum,n):
    '''This function calculates The natural sum take two
    parameters sum and n '''
    if n==0:
        return sum
    else:
        return sum_natural(sum+n,n-1)

n=int(input("enter the number: "))
print("The sum of ",n," natural numbers: ",sum_natural(0,n))
print(sum_natural.__doc__)
#resursive print of list
num=[]
m=int(input("Enter the range of list"))

for el in range(m):
    num.append(int(input("Enter the number: ")))

def print_list(lst,index):
    
    try:  
        if index==len(lst):
            return
        else:
            print(lst[index])
            print_list(lst,index+1)
    except:
        print("some error occured")
    finally:
        print("Execution completed")
        
        
    
print_list(num,0)