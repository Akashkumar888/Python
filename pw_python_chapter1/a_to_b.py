

def ato_b(a,b):
    if b==0:
        return 1
    ans=a*ato_b(a,b-1)
    return ans 
        
num1=int(input("Enter num1: "))
num2=int(input("Enter num2: "))

print(ato_b(num1,num2))
