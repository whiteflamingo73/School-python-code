#this declares the class
class RectanglePrivate:
    def __init__(self, width = 1.0, height = 2.0):#constructor sets variable values when created, will be 1 if no number is passed in
        self.__width = width  #variable is public - directly accesible outside of the class
        self.__height = height

    def getPerimeter(self):#will return the perimeter
        return (2.0 * self.__width) + (2.0 * self.__height)

    def getArea(self):#will return the area
        return self.__width * self.__height
  
    def setHeight(self, height): #allows for setting of radius, cannot be done directly
        if height > 2: #make sure radius isn't negative or 0
            self.__height = height
    
    def setWidth(self, width):
        if width > 1:
            self.__width = width

  
    def getWidth(self):#allows for access to the radius variable although it can be accessed directly as a public variable
        return self.__width
  
    def getHeight(self):
        return self.__height

    def __str__(self):#format for how the object will be printed
        return "Width: "+ str(self.__width) + " Height:"+ str(self.__height) + " | Perimeter: " + str(round(self.getPerimeter())) + " | Area: " + str(round(self.getArea()))