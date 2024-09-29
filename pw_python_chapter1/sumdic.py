
# dict.key
# dict.values

dict={
    'a':100,
    'b':200,
    'c':300
}

print(sum(dict.values()))


sum=0
for i in dict:
    sum=sum+dict[i]

print(sum)