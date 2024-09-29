

class Animal:
    def speaks(self):
       print("Generic noise")

class Dog(Animal):
    def speaks(self):
        print("Barks")

class Cat(Animal):
    def speaks(self):
        print("Meow")
        
class Cow(Animal):
    def speaks(self):
        print("Mooo")
        
                
dog=Dog()
cat=Cat()
cow=Cow()


dog.speaks()
cat.speaks()
cow.speaks()

