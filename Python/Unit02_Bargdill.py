############################################################################
# Name: Aaron Bargdill Date: 9-20-24                                       #
# Unit 2 Problems                                                          #
# Age calculator, sum of digits, initial deposit, current time.            #
############################################################################

import datetime
from datetime import timedelta, date, time
import time
#setting variables
current_time = datetime.datetime.now()
current_year = datetime.date.today().year
current_month = datetime.date.today().month
#realtime is specifically for the time.time for problem 4
realtime = time.time
#just printing the exact time and the current year
print(current_year)
print(current_time)
print("")
#goofy thing
print("Problem 1: Age Calculator")
print("")
age = input("How old will you be on your brithday this year? ")
print("")

print("WOW YOU'RE TURNING " + age + " THATS PRETTY COOL")
print("")

#actual problems:

#Problem 1. Age Calculator
print("You were born in:")
print(int(current_year) - int(age))
print("")
#the months is unnecassary, but we already figured it out, so we put it in
print("On your Birthday you will have been alive for roughly", int(age) * 12 , "months")
print("On your Birthday you will have been alive for roughly", int(age) * 365 , "days")
print("On your Birthday you will have been alive for roughly", int(age) * (365 * 24), "hours")
print("On your Birthday you will have been alive for roughly", int(age) * (365 * 24 * 60), "minutes")

"""
#Problem 1.5
#we thought this was how to do problem 2, but it wasn't but I really like it, so it's staying
print("")
#setting variables
first_number = input("give me a number between 1-1000 ")
second_number = input("give me another number between 1-1000 ")
print("The sum of those two numbers equals:", int(first_number) + int(second_number))
"""

#Problem 2.(actually): Sum of Digits
print("")
print("Problem 2: Sum of Digits")
print("")
#still need to figure out to make it only work with numbers between 0-1000
sum = 0
num = input("Give me a digit larger than 0, but smaller than 1000: ")
for digit in num:
    sum = sum + int(digit)
print("The sum of that number is", sum)

#problem 3. Initial Deposit 
print("")
print("Problem 3: Initial Deposit")
print("")
#the eval makes it an integer, for monthly interest, dividing it by 100 makes it a percentage, and then dividing it by 12
#converts it from a yearly interest rate to monthly, then for investing years, multiplying it by 12 gets you the amount of
#months in the years.
finalbalance = eval(input("What is your desired final account balance?: "))
monthlyinterest = eval(input("What is the interest rate the money will earn?: ")) / 100 / 12
investingyears = eval(input("How many years do you want to invest the money?: ")) * 12
#the {:.2f} formats it to only have 2 decimals, and .format is also needed to properly format it.
initialdeposit = ((finalbalance) / ((1 + monthlyinterest) ** investingyears))
print("The initial deposit you need to make is: ${:.2f}" .format(initialdeposit))

#problem 4. current local time
print("")
print("Problem 4: Current Local Time")
print("")
local_time = time.localtime()
formatted_time = time.strftime("%H:%M:%S", local_time) #formats time to be in military
print("The local time is", formatted_time)
