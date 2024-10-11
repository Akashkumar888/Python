
class Person:
    name="Anonymous"
    
    def changename(self,name):
        Person.name=name
        
p1=Person()

p1.changename("Akash kumar")

print(p1.name)

print(Person.name)

        