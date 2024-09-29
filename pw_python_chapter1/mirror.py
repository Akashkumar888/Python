
input_string=input("Enter string: ")
n=int(input("Enter n: "))


alphabet="abcdefghijklmnopqrstuvwxyz"
# -1 mean right to left
# 1 left to right
print(input_string)

reverse_alphabet=alphabet[::-1]
dict=dict(zip(alphabet,reverse_alphabet))

prefix=input_string[0:n-1]
suffix=input_string[n-1:]

mirror=""
for i in range(0,len(suffix)):
    mirror=mirror+dict[suffix[i]]

res=prefix+mirror
print(res)

 
