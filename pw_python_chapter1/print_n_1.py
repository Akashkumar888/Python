

def number(n):
    if n==0:
        return
    print(n)
    number(n-1)
    return


num=int(input("Enter number: "))
number(num)

