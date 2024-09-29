
c=int(input("Enter number: "))
list=(1,4,9,16,25,36,49,64,81,100)
i=0
flag=False
while i<len(list):
    if(c==list[i]):
       flag=True
    i+=1
    
    
if(flag):
    print("Yes")
else:
    print("No")
        
        