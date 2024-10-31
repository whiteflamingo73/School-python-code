import math, random

#Problem 4: Math Game (every innefficient and bulky)
correctness = 0
wrongness = 0


print("Math Game: if you get 5 right you win, but if you get 3 wrong you lose.")
print()
begin_or_not = input("Would you like to begin this game or not? type yes or no")
problem_type = input("Would you like to do addition, subtraction or both?: ")
if problem_type == "subtraction":
    neg_or_pos = input("Do you want negative answers?: ")
else:
    print()

while begin_or_not == "yes":

    num1 =(random.randint(0,9))
    num2 =(random.randint(0,9))

#this makes it do addition
    if problem_type == "addition":
        #the random.randint makes it so you can generate random problems
        
        problem_addition = (num1 + num2)

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


    if problem_type == "subtraction":
       
   #if yes makes it so you get negative, but no, gives you only positive
        if neg_or_pos == "yes":

            problem_subtraction = (num1 - num2)
   
            print("Solve this problem: ", str(num1), "-", str(num2))
            answer = eval(input())
            if answer == (problem_subtraction):
                print("correct")
                correctness = correctness + 1
            else:
                print("incorrect")
                wrongness = wrongness + 1


   #this is subtraction but with  no negative answers
        if neg_or_pos == "no":
      #this makes sure the second number is never bigger than the first so it doesn't print something that 
      #gives a negative answer
            num2 = random.randint(0,num1)

            problem_subtraction = (num1 - num2)
   
            print("Solve this problem: ", str(num1), "-", str(num2))
            answer = eval(input())
            if answer == (problem_subtraction):
                print("correct")
                correctness = correctness + 1
            else:
                print("incorrect")
                wrongness = wrongness + 1
      
#this does both addition and subtraction
    if problem_type == "both":
   #this is a random generator 1 makes it addition, while 2 makes it subtraction
            add_or_sub = random.randint(1,2)

            if add_or_sub == 1:
                problem_addition = (num1 + num2)
   
                print('Solve this problem: ', str(num1), "+", str(num2))
                answer = eval(input())
                if answer == problem_addition:
                    print("correct")
                    correctness = correctness + 1
                else:
                    print("incorrect")
                    wrongness = wrongness + 1
   
            if add_or_sub == 2:
                problem_subtraction = (num1 - num2)
   
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