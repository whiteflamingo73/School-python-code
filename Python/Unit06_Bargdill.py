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
print()

#Problem 4. is it a palindrome?
#This needs to be two functions and i need to reverse the digits
'''
def palindrome(user_digit, user_palindrome):
    
    

    if user_palindrome == True:
        print(user_digit, 'is a palindrome')

    else:
        print(user_digit, "is not a palindrome")
    print()


user_digit = str(input("Give me a number: "))
user_palindrome = str(user_digit) == str(user_digit)[::-1]
palindrome(user_digit, user_palindrome)

'''
''''
#Code Mr. Lambiase deemed bad
reverseInp = 0

def reverseInt(inp):
    reverseInp = reversed(str(inp))
    return reverseInp


def isPalindrome(inp, reverseInp):
    reverseInp == inp
    return reverseInp
'''
def reverseInt(inp):
    reverseInp = str()
    for digit in str(inp):
        reverseInp = digit + reverseInp
    return int(reverseInp)

def isPalindrome(inp):
    return int(inp) == reverseInt(inp)


inp = input("give me a number: ")



print("Your Number is a palindrome:")
print(isPalindrome(inp))


print()

#Problem 5: Palindrome Prime

def isPrime(num):
    PrimeCounter = 0
    if num > 1:
        for i in range(2, (num//2)+1):
            if (num % i) == 0:
                break
        else:
            return True
        
        
            


#All you have to do is to generate numbers(smaller to greatest) and check if it's prime, and if it's prime
#you run it through the "Is Palindrome" function, and with the returned value, you run it through numbers
#of prime, and as long as it's true, you print the number


def palindromicPrime(NumOfPrimes):
    PrimeCounter = 0
    LineCounter = 0
    num = 2
    while PrimeCounter < NumOfPrimes:
        if isPrime(num) and isPalindrome(num):
            print(f"{num:5}", end=" ")
            PrimeCounter += 1
            LineCounter += 1
            if LineCounter == 10:
                print()
                LineCounter = 0
        num += 1
    print()
    print("Done")


NumofPrimes = eval(input("How many palindromic primes do you want to see? "))
isPrime(num)
palindromicPrime(NumofPrimes)
