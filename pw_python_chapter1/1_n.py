


def number(n):
    if n==0:
        return
    number(n-1)
    print(n)
    return


num=int(input("Enter number: "))
number(num)

