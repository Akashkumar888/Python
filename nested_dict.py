
student ={
    "name" : "rahul kumar",
    "subject" : {
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}
print(len(student))
print(student["subject"]["phy"])
print('\n')
print(student.keys())
print('\n')
print(student.values())
print('\n')
print(student.items())
print('\n')
print(student["name"]) # if not present it will give error 
print('\n')
print(student.get("name")) # if not present it will give NONE 
print('\n')

newdict={
    "name":"akash kumar",
    "rollnumber":2201216
}

print(student.update(newdict))
