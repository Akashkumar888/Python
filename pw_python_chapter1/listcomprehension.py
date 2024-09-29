


# when we want to make a new list from item of an exiting list

list=[40,20,30,10,50,45,15]
print(list)
newlist=[i for i in list if i>25 ] # list comprehension
print(newlist)

# copy of list
newlist1=list.copy()
print(newlist1)

# concatenation two list
newlist1=list+newlist
print(newlist1)

# nested list
list.insert(2,[1,2,3,4,5])
print(list[2])
print(list[2][2])

