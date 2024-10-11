

class Student:
    
    college_name="ABC College"
    name="Anonymous" # class attribute 
    
    def __init__(self,name,marks):
        self.name=name  # obj attribute > class attribute
        self.marks=marks
        print("Adding new student in database: ")
        
    def welcome(self):
        print("welcome student")
        
    def getmarks(self):
        return self.marks
    
    
    # for avoid self
    @staticmethod
    def hello():
        print("hello")
            
s1=Student("Karan",98)
print(s1.name)
s1.welcome()
print( s1.getmarks() )

s1.hello()
        