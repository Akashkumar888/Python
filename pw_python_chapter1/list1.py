
fruits=["Apple","banana","cherry","mango"]
print(fruits)
print(type(fruits))

print(len(fruits))

for i in fruits:
    print(i)

if "banana" in fruits:
    print("Banana is the part of the fruits")
if "Kiwi" not in fruits:
    print("Kiwi is the not part of the fruits")
# indexing in list
    
print(fruits[2])
print(fruits[-2])

# range in index first inclusive and second exclusive

print(fruits[1:3])
print(fruits[-3:-1])


# append() -> add items to the end of the list
fruits.append("Kiwi")
print(fruits)

# insert() -> add items to the index of the list
fruits.insert(2,"Orange")
print(fruits)

# extend() -> add lists to the end of the first list
list1=[1,2,3,4]
fruits.extend(list1)
print(fruits)

# remove() -> remove specified remove item
fruits.remove("banana")
print(fruits)


# pop() -> remove item at given index or else last item
fruits.pop(1)
print(fruits)

fruits.pop()
print(fruits)

# changing item or updating item

# at an index -> 

fruits[1]=50
print(fruits)


# in a range -> 
fruits[2:4]=[20,30]
print(fruits)

# in a range -> 
fruits[2:4]="papaya"
print(fruits)

# in a range -> 
fruits[11:]=[200,300,400,500,600,700]
print(fruits)

# sorting a list
list2=[23,12,34,45,11,33,67,90,13]
print(list2)


# reverse a list
list2.reverse()
print(list2)


# ascending order
list2.sort() # by default ascending order
print(list2)


# descending order
list2.sort(reverse=True)
print(list2)




