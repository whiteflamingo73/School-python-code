import math

#this declares the class
class Rectangle:
    def __init__(self, width = 1.0, height = 2.0):#constructor sets variable values when created, will be 1 if no number is passed in
        self.width = width  #variable is public - directly accesible outside of the class
        self.height = height

    def getPerimeter(self):#will return the perimeter
        return (2.0 * self.width) + (2.0 * self.height)

    def getArea(self):#will return the area
        return self.width * self.height
  
    def setHeight(self, height): #allows for setting of radius, cannot be done directly
        if height > 2: #make sure radius isn't negative or 0
            self.height = height
    
    def setWidth(self, width):
        if width > 1:
            self.width = width

  
    def getWidth(self):#allows for access to the radius variable although it can be accessed directly as a public variable
        return self.width
  
    def getHeight(self):
        return self.height

    def __str__(self):#format for how the object will be printed
        return "Width: "+ str(self.width) + " Height:"+ str(self.height) + " | Perimeter: " + str(round(self.getPerimeter())) + " | Area: " + str(round(self.getArea()))
    #what is the 3 for?