###################################################
#Name: Aaron Bargdill                             #
#Date: 11/1/24           Unit 6                   #
#                                                 #
#Functions: Turtle Problem                        #
###################################################
import turtle
window=turtle.Screen()

myturtle=turtle.Turtle()
myturtle.speed(20)
#grid system
myturtle.goto(300,0)
myturtle.goto(-300,0)
myturtle.goto(0,0)
myturtle.goto(0,300)
myturtle.goto(0,-300)

def drawRectangle(color="black", x=0,y=0, width=30, height=30, direction=0):
    myturtle.penup()
    myturtle.color(color)
    myturtle.goto(x,y)
    myturtle.pendown()
    myturtle.fillcolor(color)
    myturtle.begin_fill() #couldve put the sqaure in a for loop, but didnt
    myturtle.left(direction)
    myturtle.forward(width)
    myturtle.left(90)
    myturtle.forward(height)
    myturtle.left(90)
    myturtle.forward(width)
    myturtle.left(90)
    myturtle.forward(height)
    myturtle.end_fill()

def drawPolygon(color="black", x=0, y=0, numsides=4, length=30):
    pass

def drawCircle(color="black", x=0, y=0, radius= 50):
    myturtle.hideturtle()
    myturtle.penup()
    myturtle.fillcolor(color)
    myturtle.color(color)
    myturtle.goto(x, y)
    myturtle.pendown()
    myturtle.begin_fill()
    myturtle.circle(radius)
    myturtle.end_fill()

#drawing the circles
drawCircle(color="green", x=150, y=-300, radius=150) # this needs to be changed to
# only show an outline to be black
drawCircle(color="black", x=150, y=-275, radius=125)
drawCircle(color="blue", x=150, y=-250, radius=100)
drawCircle(color="red", x=150, y=-225, radius=75)
drawCircle(color="yellow", x=150, y=-200, radius=50)

#drawing the squares
drawRectangle(color="red", x=10, y=5, width=300, height=300)

drawRectangle(color="green", x=10, y=153, width=212, height=212, direction=45)
drawRectangle(color="yellow", x=82, y=230, width=150, height=150, direction=45)
window.mainloop()