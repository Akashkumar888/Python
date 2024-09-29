

n=int(input("Enter n: "))

for i in range(1,n+1):
    for space in range(1,n-i+1):
        print(end=" ")
    for j in range(1,2*i-1+1):
        print(j,end="")
    print()
