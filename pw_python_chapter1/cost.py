
cost=int(input("Enter cast price: "))
sell=int(input("Enter sell price: "))

if cost==sell:
    a=sell-cost
    print("No loss No profit: ",a)
elif sell > cost:
    b=sell-cost
    print("Profit: ",b)
else:
    c=cost-sell
    print("Lose: ",c)
    