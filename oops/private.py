

class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass # for private we use __ 
        
    def reset_pass(self):
        print(self.__acc_pass)
        
    
        
acc1=Account(12345,"abcde")

print(acc1.acc_no)


print(acc1.reset_pass())


print(acc1.acc_pass)
