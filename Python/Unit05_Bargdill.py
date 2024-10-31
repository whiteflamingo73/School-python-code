############################################################
# Name : Aaron Bargdill Date: 10/17/24                     #
# Unit 5 Problems                                          #
# clock countdown, Divisible by 5 or 6,                    #
# display a pyramid, math game, Number Guessing Game       #
# random turtle                                            #
############################################################
import time, datetime, random, turtle, math 

#Problem 1: Countdown(doesn't work)
myVar = eval(input("Give me a number to countdown from: "))
for i in range(myVar,0,-1):
    time.sleep(1)
    print(i)

print()
#problem 2: Divisible by 5 or 6
count = 0
for i in range(100, 1001):
   if i % 5 == 0 or i % 6 == 0:
    if count < 9:
       print(i, end=" ")
       count = count + 1
    else:
       print(i)
       count = 0

#Problem 3: Pyramid Printing
print("")
print("Pyramid Creation")

###

userNumber = 0

while userNumber < 1 or userNumber > 15:
    userNumber = eval(input("Give me a number to make a pyramid (1-15)"))

    if userNumber < 1:
        userNumber = eval(input("Invalid input, try again (1-15)"))
    
    if userNumber > 15:
        userNumber = eval(input("Invalid input, try again (1-15)"))

#setting variables
spacer = "   "
spacer2 = " "

if userNumber > 9:
    spacer = "   "
    spacer2 = " "

spacer3 = ""

currentNum = 1

for row in range(1, userNumber + 1):
    if row == 1:
        print(spacer * (userNumber - currentNum), currentNum)
    
    elif row >= 1:
        print(spacer * (userNumber - currentNum), currentNum, end='')
        for i in range(1, currentNum):
            if (currentNum-i) < 9:
                print(spacer2, (currentNum-i), end="")

            else:
                print(spacer3, (currentNum - i), end="")
        
        for i in range(currentNum, 1, -1):
            if (currentNum - i + 2) < 9:
                print(spacer2, (currentNum - i) + 2, end='')
            
            else:
                print(spacer3, (currentNum - i) + 2, end='')
        
        print()

    currentNum += 1

print()

   
#Problem 4: Math Game (still innefficient and bulky, but less(reduced fat)) Still need to make it case insensitive
correctness = 0
wrongness = 0


print("Math Game: if you get 5 right you win, but if you get 3 wrong you lose.")
print()
begin_or_not = input("Would you like to begin this game or not? type yes or no: ")
if begin_or_not == "yes":
   problem_type = input("Would you like to do addition, subtraction or both?: ")
   if problem_type == "subtraction" or problem_type == "Subtraction" or problem_type == "S" or problem_type == "s":
      neg_or_pos = input("Do you want negative answers?: ")
else:
    print()

while begin_or_not == "yes":

    num1 =(random.randint(0,9))
    num2 =(random.randint(0,9))
    num3 = random.randint(0,num1)

    problem_addition = (num1 + num2)
    problem_subtraction = (num1 - num2) 
    problem_subtraction1 = (num1 - num3)

#this makes it do addition
    if problem_type == "addition" or problem_type == "Addition" or problem_type == "A" or problem_type =="a":
        #the random.randint makes it so you can generate random problems

        print("Solve this problem: ", str(num1), "+", str(num2))
        answer = eval(input())
        #counts how much you get right or not
        if answer == (problem_addition):
            print("correct")
            correctness = correctness + 1
        else:
            print("incorrect")
            wrongness = wrongness + 1
#makes it so you win or lose, while also breaking the loop

    if problem_type == "subtraction" or problem_type =="Subtraction" or problem_type == "S" or problem_type == "s":
       
   #if yes makes it so you get negative, but no, gives you only positive
        if neg_or_pos == "yes" or neg_or_pos == "Yes" or neg_or_pos == "Y" or neg_or_pos == "y":
            print("Solve this problem: ", str(num1), "-", str(num2))
            answer = eval(input())
            if answer == (problem_subtraction):
                print("correct")
                correctness += 1
            else:
                print("incorrect")
                wrongness += 1

   #this is subtraction but with  no negative answers
        if neg_or_pos == "no" or neg_or_pos == "No" or neg_or_pos == "N" or neg_or_pos == "n":
      #this makes sure the second number is never bigger than the first so it doesn't print something that 
      #gives a negative answer
            
   
            print("Solve this problem: ", str(num1), "-", str(num3))
            answer = eval(input())
            if answer == (problem_subtraction1):
                print("correct")
                correctness += 1
            else:
                print("incorrect")
                wrongness += + 1
      
#this does both addition and subtraction
    if problem_type == "both" or problem_type == "Both" or problem_type == "B" or problem_type == "b":
   #this is a random generator 1 makes it addition, while 2 makes it subtraction
            add_or_sub = random.randint(1,2)

            if add_or_sub == 1:
                print('Solve this problem: ', str(num1), "+", str(num2))
                answer = eval(input())
                if answer == problem_addition:
                    print("correct")
                    correctness = correctness + 1
                else:
                    print("incorrect")
                    wrongness = wrongness + 1

            if add_or_sub == 2:
                print("Solve this problem: ", str(num1), "-", str(num2))
                answer = eval(input())
                if answer == problem_subtraction:
                    print("correct")
                    correctness = correctness + 1
                else:
                    print("incorrect")
                    wrongness = wrongness + 1 
    if wrongness == 3:
        print("You lose, you got", wrongness, "wrong and only", correctness, "right.")
        break 
    if correctness == 5:
        print("You win, you got", correctness, "right, and only", wrongness, "wrong.")
        break

#Problem 5: Number guessing game

### Do a system where there's variables with a high guess and low guess, so the computer knows not to just guess higher or lower
# than just guessing higher or lower than previously
low = 1
high = 100

thinkingnumber = eval(input("Pick a number between 1-100: "))

computerguess = random.randint(low,high)

while thinkingnumber >= 1 or thinkingnumber <= 100:
   
    
    print("Is your number", computerguess, "? If it's lower type L or if it's higher type H or if it's Correct type C")
    userinput = input()
    if userinput == "L" or userinput == "l" or userinput == "lower" or userinput == "Lower":
        high = computerguess
    if userinput == "H" or userinput == "h" or userinput == "Higher" or userinput == "higher":
        low = computerguess
    if userinput == "C" or userinput == "c" or userinput == "correct" or userinput == "Correct":
        print("Yay! your number is:", computerguess)
        break

    #just to skip problem when need be:
    if userinput == "skip":
        break 
    computerguess = random.randint(low,high)

# problem 6
#turtles
myturtle = turtle.Turtle()
myturtle2 = turtle.Turtle()
myturtle3 = turtle.Turtle()
myturtle4 = turtle.Turtle()
window = turtle.Screen()
#hiding turtles
myturtle.hideturtle()
myturtle2.hideturtle()
myturtle3.hideturtle()
myturtle4.hideturtle()
#grid system
myturtle.goto(300,0)
myturtle.goto(-300,0)
myturtle.goto(0,0)
myturtle.goto(0,300)
myturtle.goto(0,-300)
#setting speed
myturtle.speed(500)
myturtle2.speed(500)
myturtle3.speed(500)
myturtle4.speed(500)

turtle.colormode(255)
#loops for shapes
for i in range(100):
    #colors
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
   

   
    #random coordinates
    circleX = random.randint(-290,-10)
    circleY = random.randint(10,290)

    etriangleX = random.randint(40,255)
    etriangleY = random.randint(40, 255)

    rtriangleX = random.randint(-265, -40)
    rtriangleY = random.randint(-270, -45)   

    lineX = random.randint(1,300)
    lineX2 = random.randint(1,300)
    lineY = random.randint(-300, -1)
    lineY2 = random.randint(-300, -1) 

    #taking action(circles)
    myturtle.pencolor(red, green, blue)
    myturtle.penup()
    myturtle.goto(circleX,circleY)
    myturtle.pendown()
    myturtle.circle(10)

    #eqilateral triangles:
    #have to set colors again so the code doesn't choose the same color for each 4 shapes
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    myturtle2.pencolor(red, green, blue)
    myturtle2.penup()
    myturtle2.home()
    myturtle2.goto(etriangleX, etriangleY)
    myturtle2.pendown()
    myturtle2.forward(60)
    myturtle2.left(120)
    myturtle2.forward(60)
    myturtle2.left(120)
    myturtle2.forward(60)

#right triangle 36 and 48
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    myturtle3.pencolor(red, green, blue)
    myturtle3.fillcolor(red, green, blue)
    myturtle3.penup()
    myturtle3.home()
    myturtle3.goto(rtriangleX, rtriangleY)
    myturtle3.pendown()
    myturtle3.begin_fill()
    myturtle3.forward(38) 
    myturtle3.left(90)
    myturtle3.forward(48)
    myturtle3.left(142)
    myturtle3.forward(60)
    myturtle3.end_fill()

    #random lines (# in this part of the loop are old parts of code I want to keep to show another solution to the problem)
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    #rlength = random.randint(50,120)
    #rdirection = random.randint(1,180)
    myturtle4.pencolor(red, green, blue)
    myturtle4.penup()
    #myturtle4.forward(rlength)
    myturtle4.goto(lineX, lineY)
    myturtle4.pendown()
    #myturtle4.right(rdirection)
    myturtle4.goto(lineX2,lineY2)






window.mainloop()