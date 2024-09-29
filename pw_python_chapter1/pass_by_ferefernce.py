
# pass by reference
# (mutable - list,dictionary)

def modifylist(lst):
    lst.append(4)
    print("Inside function list:",lst)


lst=[1,2,3]
modifylist(lst)
print("Output function list:",lst)

