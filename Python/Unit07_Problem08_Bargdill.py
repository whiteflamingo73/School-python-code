import turtle, random 

myturtle = turtle.Turtle()
window = turtle.Screen()


#want to create random word picker





mysteryWord = ["*", "*", "*", "*", "*", "*"]

correctAnswer = 0
wrongAnswer = 0

def drawHangman(num, correctAnswer, wrongAnswer, ASCIIword, copiedWord):
    
    
    
    print(TheWord)
    
    
    for i in range(6):
        if num == ASCIIword[i]:
            print("correct")
            mysteryWord.pop(i)
            #need to make this part work
            #if chr(num) == mysteryWord[i]:
            #    print("You already guessed that")
            #    correctAnswer -= 1
            mysteryWord.insert(i, chr(ASCIIword[i]))

            correctAnswer += 1
        
        if mysteryWord == copiedWord:
            print("you got the word!")
            break
        #need to make it so if there's one correct it will ignore all the wrongs
        #this part should also draw the hangman
        else:
            print("false")
            wrongAnswer += 1
        
    

    if wrongAnswer >= 6:
        print("You're Wrong")
    print(ASCIIword)
    print(num)
    print(mysteryWord)

    #print(f'corrects: {correctAnswer}')
    #print(f'wrongs: {wrongAnswer}')
    #figure out how to return the wrong and correct answers
    return(mysteryWord, wrongAnswer, correctAnswer)


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
    ['y','e','l','l','o','w']
]


TheWord = random.choice(wordbank)

ASCIIword = []
for i in range(6):
    ASCIIword.append(ord(TheWord.pop(0)))

print(TheWord)
copiedWord = TheWord.copy()
#wanna make it so you can have more than just 6 guesses

for i in range(100):
    guess = ord(input("What is your guess for a letter in the word?: "))
    drawHangman(guess, correctAnswer, wrongAnswer, ASCIIword, copiedWord)
    print(f'correct answers: {correctAnswer}, wrong answers: {wrongAnswer}')


        












window.mainloop()