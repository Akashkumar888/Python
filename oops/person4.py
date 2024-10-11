
class Person:
    name="Anonymous"
    
    @classmethod
    def changename(cls,name):
        cls.name=name
        
p1=Person()

p1.changename("Akash kumar")

print(p1.name)

print(Person.name)


        