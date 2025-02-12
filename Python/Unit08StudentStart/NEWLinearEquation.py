import turtle

class Line:

    def __init__(self, xStart, yStart, xEnd, yEnd):
        self.xStart = xStart
        self.yStart = yStart
        self.xEnd = xEnd
        self.yEnd = yEnd
        self.aline = turtle.Turtle()
    
    def drawLine(self, acolor):
        self.aline.color(acolor)
        self.aline.penup()
        self.aline.goto(self.xStart, self.yStart)
        self.aline.pendown()
        self.aline.goto(self.xEnd, self.yEnd)

        
        self.aline.penup()

    def getDeltaY(self):
        return self.yEnd - self.yStart

    def getDeltaX(self):
        return self.xEnd - self.xStart

    def getM(self):
        y = self.getDeltaY()
        x = self.getDeltaX()
        print(f"x = {x} and y = {y}")
        return y/x

    def getB(self):
        return self.yStart - (self.getM() * self.xStart)
    
    def __str__(self):
        return "Line from (%f, %f) to (%f, %f)" %( self.xStart, self.yStart, self.xEnd, self.yEnd )


class LinearEquation:

    def __init__(self, line1, line2):
        self.line1 = line1
        self.line2 = line2
        self.vertex = turtle.Turtle()
    
    def drawGraph(self):
        self.vertex.penup()
        self.vertex.color("black")
        self.vertex.goto(-300,0)
        self.vertex.pendown()
        self.vertex.goto(300,0)
        self.vertex.penup()
        self.vertex.goto(0,-300)
        self.vertex.pendown()
        self.vertex.goto(0,300)
        self.vertex.penup()
        

    def drawVertex(self):
        self.vertex.hideturtle()
        if self.line1.getM() - self.line2.getM() == 0:
            print("There is no interceting point")
        
        else:
            print(f"Intersecting Point{self.getX(), self.getY()}")
            self.vertex.penup()
            self.vertex.color("black")
            self.vertex.fillcolor("red")
            self.vertex.goto(self.getX(), self.getY()-3)
            self.vertex.pendown()
            self.vertex.begin_fill()
            self.vertex.circle(3)
            self.vertex.end_fill()
            self.vertex.penup()

    
    def isSolvable(self):
        return self.line1.getM() != self.line2.getM()
    
    def getX(self):
        return (self.line2.getB() - self.line1.getB())/(self.line1.getM() - self.line2.getM())
        
    def getY(self):
        return self.line1.getM()*self.getX() + self.line1.getB()
