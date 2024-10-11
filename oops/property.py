
class Student:
    
    def __init__(self,phy,che,math):
        self.phy=phy
        self.che=che
        self.math=math
        
    @property
    def paercentage(self):
        return    str((self.phy+self.che+self.math)/3) +"%"    
    
p1=Student(98,97,99)

print(p1.paercentage)

p1.phy=86
print(p1.paercentage)

    