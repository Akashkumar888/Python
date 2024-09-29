

# def add(n1,n2):
#     print("n1:",n1)
#     print("n2:",n2)
#     sum=n1+n2
#     return sum


# # positional argument
# print("sum of number:",add(3,2))


#keyword argument(named arguments)
# print("sum of number:",add(n2=2,n1=3))



# def add(n1=9,n2=0):
#     print("n1:",n1)
#     print("n2:",n2)
#     sum=n1+n2
#     return sum
#default argument
# print("sum of number:",add())

# def addallnumber(*args):
# args -> tuple 

#arbitrary arguments
def addallnumber(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
    
output=addallnumber(2,3,4,5,6,1)
print(output)

def studentInfo(**kwargs):
    for x,y in kwargs.items():
        print(x,"is",y)


studentInfo(Name="urvi",Age="22",city="Delhi")
studentInfo(Name="Akash",Age="23",city="Banglore")       

