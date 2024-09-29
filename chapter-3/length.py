greeting="Good morning"

name=" Harry" # space ko bhi index deta hai
print(type(name))

# concatenating two string

c=greeting + name
print(c)
print(greeting[0])
print(name[0])
print(name[1]) 
print(name[5])
# name[1]='q'    does not work

print(name[0:3])
print(greeting[:12])
print(greeting[0:])
print(greeting[0:12])