


class Parent:
    def __init__(self):
        self.super_attribute=True
        print("This is the parent class")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("This is the child class")
        print(self.super_attribute)


child1=Child()            
       