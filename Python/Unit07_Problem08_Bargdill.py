import turtle, random 

myturtle = turtle.Turtle()
window = turtle.Screen()


#want to create random word picker





mysteryWord = ["*", "*", "*", "*", "*", "*"]

incorrectLetter = ["Incorect letters:"]

wrongAnswer = [0]

def drawHangman(num, wrongAnswer, ASCIIword, copiedWord):
    
    correctAnswer = 0
    #this variable is completely useless and is just for the single if statement, I don't want to accidently break the code
    holdingVariable = 0

    
    
    for i in range(6):
        if num == ASCIIword[i]:

            mysteryWord.pop(i)
            #need to make this part work
            #if chr(num) == mysteryWord[i]:
            #    print("You already guessed that")
            mysteryWord.insert(i, chr(ASCIIword[i]))
            correctAnswer += 1

        
       
        
        #need to make it so if there's one correct it will ignore all the wrongs
        #this part should also draw the hangman
        else:
            holdingVariable += 1

    #counts how many wrong guesses you've had and also adds 
    if correctAnswer == 0:
        wrongAnswer[0] += 1
        incorrectLetter.append(chr(num))
        print(incorrectLetter)

        

    if mysteryWord == copiedWord:
        print("you got the word!")

    #The wrong guesses(drawing the hangman):

    if wrongAnswer[0] == 1:
        myturtle.penup()
        myturtle.goto(0,150)
        myturtle.pendown()
        myturtle.circle(50)

    if wrongAnswer[0] == 2:
        myturtle.goto(0,0)
    
    if wrongAnswer[0] == 3:
        myturtle.penup()
        myturtle.goto(0,140)
        myturtle.pendown()
        myturtle.goto(-50,140)
    
    if wrongAnswer[0] == 4:
        myturtle.goto(50,140)
    
    if wrongAnswer[0] == 5:
        myturtle.penup()
        myturtle.goto(0,0)
        myturtle.pendown()
        myturtle.goto(-25,-50)

    if wrongAnswer[0] >= 6:
        print("You Lost")
        myturtle.penup()
        myturtle.goto(0,0)
        myturtle.pendown()
        myturtle.goto(25,-50)
        myturtle.color("red")
        myturtle.write("Game Over")
        

    print("The Mystery Word:", mysteryWord)

    

    
    return mysteryWord, wrongAnswer


wordbank = [
    ['d', "r", "a","g","o","n"],
    ['s', 't', 'o','r','e','s'],
    ['l','a','n','d','y','n'],
    ['p','r','i','n','c','e'],
    ['a','d','v','i','c','e'],
    ['j','a','z','z','e','d'],
    ['w','i','z','a','r','d'],
    ['q','u','a','r','t','z'],
    ['z','o','m','b','i','e'],
    ['p','a','z','a','z','z'],
    ['y','e','l','l','o','w'],
    ['d','a','b','b','l','e'],
    ['f','a','b','r','i','c'],
    ['h','a','b','i','t','s'],
    ['r','a','b','b','i','t'],
    ['m','a','c','h','e','s'],
    ['m','a','c','a','w','s'],
    ['m','a','n','g','o','s'],
    ['p','a','c','i','f','y'],
    ['t','a','b','l','e','s'],
    ['u','g','l','i','f','y'],
    ['v','a','c','u','u','m'],
    ['v','a','c','a','t','e'],
    ['w','a','c','k','e','d'],
    ['y','a','c','h','t','s']
]


TheWord = random.choice(wordbank)


copiedWord = TheWord.copy()
#wanna make it so you can have more than just 6 guesses


ASCIIword = []
for i in range(6):
    ASCIIword.append(ord(TheWord.pop(0)))



print("This is hangman, all words are 6 letters, and if you get 6 guesses wrong, you lose")

for i in range(100):
    guess = ord(input("What is your guess for a letter in the word?: "))
    drawHangman(guess, wrongAnswer, ASCIIword, copiedWord)
    if wrongAnswer[0] == 6:
        print(f"The word was{copiedWord}")
        break
    if mysteryWord == copiedWord:
        break


        












window.mainloop()