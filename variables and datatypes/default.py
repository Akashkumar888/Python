
# Equivalent to: sayname(fname="ankit", lname=None)
def sayname(fname="ankit", lname=None):
    print("My name is:", fname, lname if lname else "")

sayname("akash")  # Outputs: akash

# Equivalent to: sayname(fname="ankit", lname="surya")
def sayname2(fname="ankit", lname="surya"):
    print("My name is:", fname, lname)

sayname2("akash")  # Outputs: akash surya

# Equivalent to: sayname(fname, lname="surya")
def sayname3(fname, lname="surya"):
    print("My name is:", fname, lname)

sayname3("akash")  # Outputs: akash surya

# Equivalent to: sayname(fname, lname)
def sayname4(fname, lname):
    print("My name is:", fname, lname)

sayname4("akash", "kumar")  # Outputs: akash kumar
