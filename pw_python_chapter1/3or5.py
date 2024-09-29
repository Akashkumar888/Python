
num=int(input("Enter the number: "))
if num%15==0:
    print("Number is divisible by 15")
else:
    if num%3==0 or num%5==0:
     print("Number is divisible by 3 or 5 but not 15")
    else:
       print("Neither divisible by 3 or 5")
