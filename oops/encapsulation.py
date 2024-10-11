class Car:
    def __init__(self):
        # Private attributes with double underscore
        self.__accelerator = False
        self.__brk = False
        self.__clutch = False
        
    # Public method to start the car
    def start(self):
        self.__clutch = True
        self.__accelerator = True
        print("Car started")
    
    # Public method to apply the brake
    def apply_brake(self):
        self.__brk = True
        print("Brake applied")
    
    # Getter methods to access private attributes (read-only)
    def is_accelerator_on(self):
        return self.__accelerator
    
    def is_brake_on(self):
        return self.__brk
    
    def is_clutch_on(self):
        return self.__clutch

# Creating a car object and using its methods
c1 = Car()
c1.start()

# Accessing the private attributes through getter methods
print(f"Accelerator on: {c1.is_accelerator_on()}")
print(f"Brake on: {c1.is_brake_on()}")
print(f"Clutch on: {c1.is_clutch_on()}")

# Applying brake
c1.apply_brake()
print(f"Brake on after applying: {c1.is_brake_on()}")
