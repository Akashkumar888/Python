# creating tuple in python
# ordered
# immutable
# duplicate allowed
# any datatypes
# mix of different data types

colours=("blue","red","green","orange")
print(colours)

# creating a tuple with 1 item
fruits=("Apple",) # , necessary
print(fruits)
fruits=tuple(("banana"))
print(fruits)


# check type of tuple
print(type(fruits))
print(type(colours))


# length of the tuple
print(len(colours))


#accessing item in tuple
print(colours[0]) # positive index
print(colours[-3]) # negative index
print(colours[1:3]) # positive range index
print(colours[-3:-1]) # negative range index

# check item is exist or not in tuple
if "blue" in colours:
    print("blue is the part of the tuple")
if "black" not in colours:
    print("black is not part of the tuple")

# traverse in the tuple
for i in colours:
    print(i,end=" ")
print()

# concatenate two tuple
more_colours=("Yellow","Brown")
colours=colours+more_colours
print(colours)

#unpacking in tuple

number=(1,2,3,4)
num1 ,num2,num3,num4=number
print(num1)
print(num2)
print(num3)
print(num4)

