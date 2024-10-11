class Complex:
    
    def __init__(self,real,img):
        self.real=real
        self.img=img
        
    def show(self):
        print(self.real,"+",self.img,"i")
    
    
    def __add__(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self,num2):
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return Complex(newReal,newImg)

num1=Complex(2,7)
num1.show()
        
num2=Complex(4,5)
num2.show()        

num3=num1+num2
num3.show()

num4=num1-num2
num4.show()

