
a1=[1,5,10,20,40,80]
a2=[6,7,20,80,100]
a3=[3,4,15,20,30,70,80,100]

s1=set(a1)
s2=set(a2)
s3=set(a3)

s4=s1.intersection(s2)
s5=s3.intersection(s4)

a4=list(s5)
print(a4)


