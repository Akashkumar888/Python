
class Car:
    @staticmethod
    def start():
        print("Car started..")
    
    @staticmethod
    def stop():
        print("Car stoped..")
        
class ToyotoCar(Car):
    def __init__(self,name):
        self.name=name
        
car1=ToyotoCar("Fortuner")
car2=ToyotoCar("Prius")

print(car1.name)

print(car1.start())
                    