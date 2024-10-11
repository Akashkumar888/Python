


class Car:
    color="Blue"
    brand="Tata"
    #default constructor
    def __init__(self):
        pass
    
    def __init__(self,name):
        self.name=name 
        print("Adding new student in database: ")

c1=Car("BMW")
print(c1.name)

c2=Car("Mercedes")
print(c2.name)


