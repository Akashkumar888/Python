
# built-in function

def factorial(n):
    if n==0: 
       return 1
    fact=1
    for i in range(2,n+1):
     fact=fact*i
    return fact

n=int(input("Enter the number:"))
print("Factorial of ",n," is :",factorial(n))

