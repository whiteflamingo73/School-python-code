import turtle

class Line:

  def __init__(self, xStart, yStart, xEnd, yEnd):
    self.__xStart = xStart
    self.__yStart = yStart
    self.__xEnd = xEnd
    self.__yEnd = yEnd
    self.__aline = turtle.Turtle()

  #draw the line with the given end points
  def drawLine(self, acolor):
    #completed by student
    pass

  #get the difference in y values for the slope formula
  def getDeltaY(self):
    #completed by student
    pass

  #get the difference in x values for the slope formula
  def getDeltaX(self):
    #completed by student
    pass

  #calculate and return the slope of the line
  def getM(self):
    #completed by student
    pass

  #calculate and return the Y intercept, where the line crosses the Y axis
  def getB(self):
    #completed by student
    pass

  #create a string value for the line for printing object
  def __str__(self):
    return "Line from (%f, %f) to (%f, %f)" %( self.__xStart, self.__yStart, self.__xEnd, self.__yEnd )


class LinearEquation:

  def __init__(self, line1, line2):
    self.__line1 = line1
    self.__line2 = line2
    self.__vertex = turtle.Turtle()

  #draws cartesian coordinate x&y axis
  def drawGraph(self):
    #completed by student
    pass

  #draw a circle at the intersecting point
  def drawVertex(self):
    #bug fixed by student
    #draw a 2 pixel cirlce at the intersecting point of the two lines
    print("Intersecting Point:", self.getX(), self.getY())
  
  #Checks to make sure the slopes are not the same
  def isSolvable(self):
    return self.__line1.getM() != self.__line2.getM()
  
  #get the x value of the intersecting point
  def getX(self):
    #bug fixed by student
    return (self.__line2.getB() - self.__line1.getB())/(self.__line1.getM() - self.__line2.getM())

  #get the y value of the intersecting point
  def getY(self):
    #bug fixed by student
    return self.__line1.getM()*self.getX() + self.__line1.getB()

