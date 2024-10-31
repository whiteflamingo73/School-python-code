#Problem 2.(actually): Sum of Digits
print("")
#still need to figure out to make it only work with numbers between 0-1000
sum = 0
num = input("Give me a digit larger than 0, but smaller than 1000: ")
for digit in num:
    sum = sum + int(digit)
print("The sum of that number is", sum)