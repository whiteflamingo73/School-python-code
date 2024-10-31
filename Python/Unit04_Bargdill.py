############################################################################
# Name : Aaron Bargdill Date: 10-7-24                                      #
# Unit 4 Problems                                                          #
# Sort 3 sort three numbers, divisible by 5 and/or 6                       #
# Rock, Paper, or Scissors, Pick a card                                    #
# Palindrome Number, turtle overlap                                        #
############################################################################

import random 
import turtle
#Problem 1: Sort three numbers from smallest to largest 
#variables, a corresponds to the first number, b to the second, and c to the third
a, b, c = eval(input("Enter three numbers split by commas: "))

if a < b < c:
    print(a, b, c)
if a < c < b:
    print(a, c, b)
if b < a < c:
    print(b, a, c)
if b < c < a:
    print(b, c, a)
if c < b < a:
    print(c, b, a) 
if c < a < b:
    print(c, a, b)   

#Problem 2: is it divisible by 5 or 6???

divisiblenum = eval(input('Give me a random number: '))
#checking if it's divisible by 5
if divisiblenum %5==0:
    print('It is divisible by 5')
else:
    print('It is not divisible by 5')
#checking if it's divisible by 6
if divisiblenum %6==0:
    print('It is divisible by 6')
else:
    print('It is not divisible by 6')

#Problem 3: Rock! Paper! Scissors! Shoot!

rock, paper, scissors = 0, 1, 2
player_input = eval(input('Rock, Paper, or Scissors; CHOOSE ONE NOW! '))
computer_input = (random.randint(0,2))

if player_input == 0:
    if computer_input == 0:
        print("It's a draw, I picked rock too")
    if computer_input == 2:
        print('You win, I picked scissors')
    if computer_input == 1:
        print('HA! You lose, I picked paper')

if player_input == 1:
    if computer_input == 1:
        print("It's a draw, I picked paper")
    if computer_input == 2:
        print('HA! You lose, I picked scissors')
    if computer_input == 0:
        print('You win, I picked rock')

if player_input == 2:
    if computer_input == 2:
        print("It's a draw, I picked scissors")
    if computer_input == 1:
        print("You win, I picked paper")
    if computer_input == 0:
        print ("HA! You lose, I picked rock")
        
#Problem 4 Random Card Generator 

cardnumber = (random.randint(1,13))
cardsuit = (random.randint(1,4))

#Determining card number, and printing it differently if need be
if cardnumber == 1:
    cardnumber = str('Ace')

if cardnumber == 11:
    cardnumber = str('Jack')

if cardnumber == 12:
    cardnumber = str('Queen')

if cardnumber == 13:
    cardnumber = str('King')

#determining card suit
if cardsuit == 1:
    cardsuit = str('Spades')

if cardsuit == 2:
    cardsuit = str('Clubs')

if cardsuit == 3:
    cardsuit = str('Hearts')

if cardsuit == 4:
    cardsuit = str('Diamonds')

#printing the final result
print()
print('Random Card Generator:')
print(cardnumber, 'of', cardsuit)
print()

#Problem 5: Palindrome or not?
#user_palindrome is determining if it is equal to the opposite of the user input, the [::-1] is reversing the number
three_digit = str(input("Give me a three digit number: "))
user_palindrome = str(three_digit) == str(three_digit)[::-1]

if user_palindrome == True:
    print(three_digit, 'is a palindrome')

else:
    print(three_digit, "is not a palindrome")
print()

#Problem 6: Turtle Circle Overlap 
window = turtle.Screen()
myturt1 = turtle.Turtle()
writingturtle = turtle.Turtle()
redcircle = turtle.Turtle()
#hiding of the turtles
myturt1.hideturtle()
writingturtle.hideturtle
redcircle.hideturtle()
#coordinate grid:
myturt1.goto(250,0)
myturt1.goto(-250,0)
myturt1.goto(0,0)
myturt1.goto(0,250)
myturt1.goto(0,-250)
#getting a red cirlce in the center
myturt1.goto(0,0)
myturt1.dot(22)
myturt1.color('red')
myturt1.dot(18)
myturt1.color('black')
#user input circles
myturt1.penup()
coord1, coord2, radius = eval(input("Give me two numbers for coordinates, and a circle radius, make sure it's seperated by a commas: "))
myturt1.goto(coord1, coord2)
myturt1.pendown()

myturt1.circle(radius)

myturt1.penup()
coord3, coord4, radius2 = eval(input("Give me another set of coordinates, and radius: "))
myturt1.goto(coord3,coord4)
myturt1.pendown()
myturt1.circle(radius2)

#determining if the circles overlap or not
overlap = (((coord3 - coord1) ** 2) + ((coord4 - coord2) ** 2)) ** 0.5

if overlap < radius - radius2:
    myturt1.write("The first circle is inside the other circle")

elif overlap > radius + radius2:
    myturt1.write("The circles are not touching")
    
else:
    myturt1.write("The circles are overlpaing")


#keeping the window open
window.mainloop()