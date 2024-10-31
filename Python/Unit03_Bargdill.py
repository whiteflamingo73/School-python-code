############################################################################
# Name : Aaron Bargdill Date: 9-30-24                                      #
# Unit 3 Problems                                                          #
# ASCII Characters, payroll application, random uppercase letter,          #
# String Methods, Turtle Olympic Rings                                     #
############################################################################

#importing stuff needed for the problems
import time
import turtle
print("ASCII CHARACTERS")
#problem 1. ASCII CHARACTERS 

uppercharcter = eval(input("Give me a number between 65-90: "))
lowercharacter = eval(input("Now give me a number between 97-122: "))

#print("Those two characters in ASCII are:", chr(int(uppercharcter)) ,"and", chr(int(uppercharcter + 65)))
print("Your first number's ASCII character is: ", chr(uppercharcter))
print("And here's the lowercase character:", (chr(uppercharcter + 32)))
print()
print("Your second number's ASCII character is: ", chr(lowercharacter))
print("And here's the uppercase character:", (chr(lowercharacter - 32)))

#Problem 2. Finnancial Application
print()
print("Payroll Application:")
print()
#setting variables
EmployeeName = input("What's your name? ")
WorkWeek = eval(input("How many hours do you work a week? "))
HourPay = eval(input("How much money do you get payed per hour? "))
FederalTax = eval(input("What's the Federal Tax rate as a percent? ")) / 100
StateTax = eval(input("What's the State Tax rate as a percent? ")) / 100
print()
print("Hours Worked:", WorkWeek)
print("Hourly Pay Rate:", HourPay)
print("Gross Pay:", WorkWeek * HourPay)

print("Federal Withholding:", FederalTax * 100,"%:", "$", (WorkWeek * HourPay) * FederalTax)
print("State Withholding", StateTax * 100, "%:", "$" ,(WorkWeek * HourPay) * StateTax)
print("Total Deduction:", "$", ((WorkWeek * HourPay) * FederalTax) + ((WorkWeek * HourPay) * StateTax))
#basically figuring out how much your total pay is and then subtracting the taxes
print(EmployeeName, "Your Net Pay is", "$",(WorkWeek * HourPay) - (((WorkWeek * HourPay) * FederalTax) + ((WorkWeek * HourPay) * StateTax)), "A Week")
print()

#Problem 3: Getting a random letter using time, and then return the letter as a number value on the ASCII table
print("Problem 3: Generating a Random Letter")
print()
timeNow = time.time()
print(timeNow)

modTime = int(timeNow % 26)
adjustedValue = (modTime + 65)
print("The random number is:",adjustedValue)
print("The letter is:", chr(adjustedValue))
print()

#Problem 4: String methods
print("Problem 4: String Methods")
print()
#princ is the variable for princiPle, i just didn't want to type out that word exactly for it
princ = ("princiPle")
princ = (princ.replace("Ple", "pal"))
princ = (princ.capitalize())
print(princ)

#Problem 5: Olympic Rings
#setting the variables, turtles are kinda confusing with their numbers, it's no longer the order at which they draw because I had to reorder the code
window = turtle.Screen() 
turtle.title("Problem 5: Olympic Rings")
myturtle =turtle.Turtle()
myturtle2 = turtle.Turtle()
myturtle3 = turtle.Turtle()
myturtle4 = turtle.Turtle()
myturtle5 = turtle.Turtle()

#creating the seperate rings
#blue turtle:
myturtle.pensize(4)
myturtle.color("blue")
myturtle.circle(50)
#yellow turtle
myturtle4.pensize(4)
myturtle4.penup()
myturtle4.goto(56,-50)
myturtle4.pendown()
myturtle4.color("gold1")
myturtle4.circle(50)
#black turtle
myturtle2.pensize(4)
myturtle2.penup()
myturtle2.goto(110,0)
myturtle2.pendown()
myturtle2.color("black")
myturtle2.circle(50)
#green turtle
myturtle5.pensize(4)
myturtle5.penup()
myturtle5.goto(170,-50)
myturtle5.pendown()
myturtle5.color("green")
myturtle5.circle(50)
#red turtle
myturtle3.pensize(4)
myturtle3.penup()
myturtle3.goto(220,0)
myturtle3.pendown()
myturtle3.color("red")
myturtle3.circle(50)

#positioning turtles to create correct ring order

#blue turtle
myturtle.penup()
myturtle.goto(50,53)
myturtle.left(90)

#yellow turtle
myturtle4.penup()
myturtle4.goto(65,51)

#black turtle
myturtle2.penup()
myturtle2.goto(160,53)
myturtle2.left(90)

#green turtle
myturtle5.penup()
myturtle5.goto(175,51)

#keeping the window open
window.mainloop()