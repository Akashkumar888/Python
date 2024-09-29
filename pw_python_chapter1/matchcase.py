
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

operator=(input("Enter operator: "))
match operator:
    case '+':
        print("Sum of two number: ",num1+num2)
    case '-':
        print("Subtraction of two number: ",num1-num2)
    case '*':
        print("Product of two number: ",num1*num2)
    case '/':
        print("Division of two number: ",num1/num2)
    case _ :
        print("Enter a valid operator")
        
