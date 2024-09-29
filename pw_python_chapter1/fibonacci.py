
def fibonacci(n):
    if n==1 :
        return 0
    if n==2:
        return 1
    ans=fibonacci(n-1)+fibonacci(n-2)
    return ans

num=int(input("Enter the number: "))
print(fibonacci(num))
