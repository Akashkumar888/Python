
n=int(input("Enter the size of list: "))
list=[]
for _ in range(n):
    num=int(input("Enter element: "))
    list.append(num)

idx1=int(input("Enter index1: "))
idx2=int(input("Enter index2: "))


print(list)

for i in list:
    temp=list[idx1]
    list[idx1]=list[idx2]
    list[idx2]=temp

print(list)


