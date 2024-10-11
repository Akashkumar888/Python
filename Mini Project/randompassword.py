
import random
import string

pass_len=12
charValue=string.ascii_letters+string.digits+string.punctuation

password=""

for i in range(12):
    password+=random.choice(charValue)

print("Your random password is: ", password)


 