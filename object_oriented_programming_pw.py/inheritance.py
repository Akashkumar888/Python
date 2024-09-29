

class Parent:
    def __init__(self):
        print("This is the parent class")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("This is the child class")



child1=Child()            
       