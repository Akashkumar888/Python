
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))

max= a if (a>b and a>c ) else  b if(b>a and b>c) else c
print("Maximum number: ",max)

