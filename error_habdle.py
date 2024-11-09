
try:
    print("try block start here:")
    print(x)  # x is not defined, will raise NameError
    print("try block ends here:")
except Exception as e:
    print("I am inside catch block")
