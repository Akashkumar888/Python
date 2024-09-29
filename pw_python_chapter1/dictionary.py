
# store key value in pairs
# ordered
#changeable
#unindexed
#duplicate not allowed for keys
#any datatype


phones={
    "jhon":12345,
    "ria":345678,
    "joy":678903
}
print(phones)


print(type(phones))


print(len(phones))


print(phones["jhon"])
print(phones.get("jhon"))
print(phones.keys())

phones["jhon"]=987654
print(phones)

phones["sia"]=23451232
print(phones)

more_phones={
    "pia":1829384
}
phones.update(more_phones)
print(phones)


# #remove element

# phones.pop("jhon")
# print(phones)

# phones.popitem()# this will remove last added item
# print(phones)

# phones.clear() #this will empty dict
# print(phones)


#printing values of dictionay


# for i in phones:
#     print(i)



# for i in phones:
#     print(phones[i])


# for i in phones.items():
#     print(i)



for x,y in phones.items():
    print(x,y)

phones12={
    "area1":{
        "a":1,
        "b":2,
        "c":3
    },
    "area2":{
        "x":4,
        "y":5,
        "z":6
    }
}

print(phones12['area1']["b"])
print(phones12['area2']["y"])

