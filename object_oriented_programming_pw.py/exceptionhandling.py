

a=int(input("Enter a:"))
b=int(input("Enter b:"))

try:
    result=a/b
except ZeroDivisionError:
    result=None
    print("Error: cannot Divide By Zero")   
finally:
    print("Division operator completed",result)

