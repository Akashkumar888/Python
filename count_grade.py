
grade=['C','D','A','A','B','B','A']

print(grade.count('A'))

n=len(grade)
count=0

for i in range(n):
    if(grade[i]== 'A'):
        count=count+1

print(count)        

count=0
for i in grade:
    if(i== 'A'):
        count=count+1

print(count)        
