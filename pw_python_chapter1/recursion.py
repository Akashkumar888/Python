

# the function definition def recurse()

def factorial( n):
 
 # base case
 if n==0 or n==1:
  return 1
 
 # recursive case 
 ans=n*(factorial(n-1))
 return ans



num=int(input("Enter the number: "))
print(factorial(num))
 