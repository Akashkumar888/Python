
n=int(input("Enter n: "))
sum=n*(n+1)/2
print(sum)


# blocks of reusable code 
# that perform a specific task
sum1=0
for i in range(1,n+1):
    sum1+=i
print(sum1)

# types of function
# built-in
# user defined

def printhello():
    print("Hello world")

printhello()
