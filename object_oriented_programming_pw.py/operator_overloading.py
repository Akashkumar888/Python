
class ComplexNumber:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def __add__(self,other):
        return ComplexNumber(self.real+other.real,self.img+other.img) 


c1=ComplexNumber(2,3)
c2=ComplexNumber(5,6)
c3= c1 + c2

print(c3.real," + ",c3.img,"i")
