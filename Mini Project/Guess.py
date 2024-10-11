
import random

target=random.randint(1,100)

while True:
    usernum=int(input("Enter user number: "))
    
    if(usernum==target):
        print("Guess Correct")
        break
    elif(usernum<target):
        print("your number was too small. Take a bigger guess..")
    else:
        print("your number is too large. Take a smaller guess.. ")
        
print("-----GAME OVER-----")
            