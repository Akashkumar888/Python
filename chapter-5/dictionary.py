mydict={
    "fast": "In a quick manner",
    "Harry":"A coder",
    "marks":[1,2,3,4],
    "anotherdict":{'harry': "player"}
}
print(mydict['fast'])
print("\n")
print(mydict['Harry'])
print("\n")
print(mydict['marks'])
print("\n")
mydict['marks']=[34,56]
print(mydict['marks'])
print(mydict["anotherdict"])

print(mydict["anotherdict"]['harry']) # nested dictionary

