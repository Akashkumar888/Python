
class Employee:
    
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
        
    def showDetails(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)
    
class Engineer(Employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("Engineer","IT","80,000")
        
            
            
        
e1=Employee("Accountant","Finance","60,000")
e1.showDetails()

eng1=Engineer("Akash kumar",24)
eng1.showDetails()

            