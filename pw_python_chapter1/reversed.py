
alphabet=('a','b','c','d','e','f','g')
print(alphabet)
list=[]
for i in reversed (alphabet):
    list.append(i)

alphabet=tuple(list) # type casting

print(alphabet)

