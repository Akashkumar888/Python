

class Rectangle:

    def __init__(self,heights,width):
      print(f"A rectangle is created with height: {heights} and width:{width}")
      self.heigths=heights
      self.width=width 
         
      def set_dimensions(self,heights,width):
            self.heights=heights
            self.width=width

      def area(self):
            return self.width*self.heights
      def permeter(self):
            return 2*(self.heights+self.width)
      

# creating a objects
recatangle1=Rectangle(4,3)
recatangle2=Rectangle(5,6)
recatangle3=Rectangle(7,8)
recatangle4=Rectangle(3,9)
