

class Rectangle:
      def set_dimensions(self,heights,width):
            self.heights=heights
            self.width=width

      def area(self):
            return self.width*self.heights
      def permeter(self):
            return 2*(self.heights+self.width)
      

# creating a objects
heights=int(input("Enter height: "))
width=int(input("Enter width: "))      
recatangle1=Rectangle()
recatangle1.set_dimensions(heights,width)
print(recatangle1.heights,recatangle1.width)

print("The area is: ",recatangle1.area())
print("The perimetre is: ",recatangle1.permeter())

