
# # sets 
# # container for storing multiple data
# # unordered
# # immutable
# # unindexed
# # duplicate not allowed
# # any datatypes
# # mix of different data types

# # can not update existing values 
# # remove and add allow

# names={"sia","mia","tia"}
# print(names)


# print(len(names))
# print(type(names))

# for i in names:
#     print(i)

# if "sia" in names:
#     print("Sia is present in sets")

# if "kia" not in names:
#     print("kia is present in sets")

# names.add("ria")
# print(names)
# names.add("sia")
# print(names)

# names_list=["pia","lia"]
# names.update(names_list)
# print(names)

# #removing from set
# names.remove("tia")
# print(names)

# # jb element na present ho
# names.discard("qia")
# print(names)

s1={'a','b','c'}
s2={'d','e','a'}
# print(s1,s2)

# print( s1.union(s2) )
# print(s1.intersection(s2))
# s1.intersection_update(s2)
# print(s1)

# s1.update(s2)
# print(s1)

print(s1.difference(s2))
print(s2.difference(s1))

s1.symmetric_difference_update(s2) # s1,s2 difference udate krke s1 me
print(s1)

