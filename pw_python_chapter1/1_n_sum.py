



def sum1_n(n):
    sum=0
    if n==0:
        return 0
    sum=n+sum1_n(n-1)
    return sum


num=int(input("Enter number: "))
print(sum1_n(num))


