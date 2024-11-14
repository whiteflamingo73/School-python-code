###################################################
#Name: Aaron Bargdill                             #
#Date: 11/1/24           Unit 6                   #
#                                                 #
#Functions: sum of digits. sort 3 numbers, display#
# characters, palindrome prime, emrip, turtle draw#
# shapes                                          #
###################################################

import math, random, turtle

#problem 1: Sum of digits


num = 0
def sum_of_digits(numb):
    num = eval(input("Give me a digit larger than 0: "))
    sum = 0
    for digit in str(num):
        sum = sum + int(digit)
    print("The sum of that number is", sum)


sum_of_digits(num)
print()

#problem 2: sort three numbers

def SortingNumbers(a, b, c):

    if a < b < c:
        return(a, b, c)
    if a < c < b:
        return(a, c, b)
    if b < a < c:
        return(b, a, c)
    if b < c < a:
        return(b, c, a)
    if c < b < a:
        return(c, b, a) 
    if c < a < b:
        return(c, a, b)


a, b, c = eval(input("Enter three numbers split by commas: "))
print(SortingNumbers(a, b, c))



def printChars(ch1, ch2, numPerLine):
    counter = 0
    
    if ord(ch2) > ord(ch1):
        for letter in range(ord(ch1), ord(ch2) + 1):
            print(chr(letter), end=" ")
            counter += 1
            if counter >= numPerLine:
                print()
                counter = 0
    if ord(ch1) > ord(ch2):
        for letter in range(ord(ch2), ord(ch1) + 1):
            print(chr(letter), end=" ")
            counter += 1
            if counter >= numPerLine:
                print()
                counter = 0
    

ch1 =(input("Enter a letter: "))
ch2 = input("Enter another letter: ")
numPerLine = eval(input("Enter a number for how many letters you want displayed per line: "))
print()

printChars(ch1, ch2, numPerLine)

#Problem 4. is it a palindrome?

def palindrome(user_digit, user_palindrome):
    
    

    if user_palindrome == True:
        print(user_digit, 'is a palindrome')

    else:
        print(user_digit, "is not a palindrome")
    print()


user_digit = str(input("Give me a three digit number: "))
user_palindrome = str(user_digit) == str(user_digit)[::-1]
palindrome(user_digit, user_palindrome)

