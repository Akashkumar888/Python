

# # for converting character to uppercase

# str1="new york"
# str2=str1.upper()
# print(str2)


# # for converting character to lowercase
# str3="Akash kumar"
# str4=str3.lower()
# print(str4)

# # for capitalizing first character in my string
# str5=str4.capitalize()
# print(str5)


# for removing/stripping any triling whitespace

# str1="      hello world!         "
# print(str1.strip())
# print(str1)


# # replacing word
# str="Hello world, what a beautiful  world this is"
# print(str.replace("world","earth"))
# print(str.replace("world","solarsystem",1))


# splitting string
# str1="ria sia tia mia pia"
# list1=str1.split()
# print(list1)


# str2="ria,sia,tia,mia,pia"
# list2=str2.split(",")
# print(list2)

# str3="ria,sia,tia,mia,pia"
# list3=str3.split(",",2)
# print(list3)


#concatenation our string

# str1="hello world!"
# str2="what a great place this is"
# print(str1+str2)


# string formatting

student_name="Pallavi"
student_marks=98

str1="The student name is {s}, and marks is {m}".format(s=student_name,m=student_marks)
print(str1)

