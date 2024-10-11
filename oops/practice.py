
class Student:
    
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+= val   
        
        print("Hii",self.name,"your avg score is: ", sum/3)
        


s1=Student("Akash",[98,97,96])
s1.get_avg()

s2=Student("karan",[95,93,99])
s2.get_avg()

s3=Student("shubham",[99,94,96])
s3.get_avg()

     