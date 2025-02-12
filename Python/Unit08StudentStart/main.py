

############################ ONE ########################
def prob1():
  from Rectangle import Rectangle
  from RectanglePrivate import RectanglePrivate

  print("\n\n")
  print("Problem #1 - Rectangle Class\n")

  rect1 = Rectangle(4,40)
  print("Width:", rect1.width, "| Height:", rect1.height, "| Area:", rect1.getArea(), "| Perimeter:",rect1.getPerimeter())
  print(rect1, "\n")

  print("\n")
  
  rect2 = RectanglePrivate(20.5,35.5)
  #print(f"Width: {rect2.__width}, | Height: {rect2.__height}, | Area: {rect2.getArea()}, | Perimeter: {rect2.getPerimeter()}")
  print(rect2, "\n")

  print("Change width of public rectangle variable directly to 20")
  rect1.width = 20
  print(rect1, "\n")

  print("Try to change the width of private rectangle to 70")
  rect2.__width = 70
  print(rect2, "\n")

  print("Change width variable with set method to 25.0")
  rect2.setWidth(25.0)
  print(rect2, "\n")







############################ TWO ########################
def prob2():
  from Account import Account

  print("\n\n")
  print("Problem 2: Account")
  print()
  user = Account("Aaron", 2000, 1000)
  print(user, "\n")
  print()

  print("Trying to deposit -200 into checking")
  user.checkingDeposit(-200)
  print(user, "\n")
  print()

  print("Deposit 200 into checkings")
  user.checkingDeposit(200)
  print(user, "\n")

  print()

  print("Try to withdraw 5000")
  user.checkingWithdrawl(5000)
  print(user, "\n")

  print()

  print("Try to withdraw -1000")
  user.checkingWithdrawl(-1000)
  print(user, "\n")

  print("Withdraw 500")
  user.checkingWithdrawl(500)
  print(user, "\n")

  print()
  print("Try to deposit into savings -200")
  user.savingsDeposit(-200)
  print(user, "\n")

  print()
  print("Deposit 200 into savings")
  user.savingsDeposit(200)
  print(user, "\n")

  print()
  print("Try to withdraw 5,000 from savings")
  user.savingsWithdrawl(5000)
  print(user, "\n")

  print()
  print("Withdraw 500 from savings")
  user.savingsWithdrawl(500)
  print(user, "\n")

  print()
  print("Withdraw 1800 from checking")
  user.checkingWithdrawl(1800)
  print(user, "\n")
  






############################## THREE #################################
def prob3():
  from Student import Student
  student = Student()

  student.setName()

  
  studentGrade = input("What is your graduating year? ")
  student.setGradYear(studentGrade)

  studentTown = str(input("What town are you from? "))
  student.setTown(studentTown)

  AddingClasses = True
  while AddingClasses == True:
    aClass = input("Give a class you're in: ")

    aScore = input("Give the score you have in the class you just entered: ")

    student.addClass(aClass, aScore)

    Continue = input("Do you want to add more classes? input YES or NO ")
    if Continue == "YES" or Continue == "yes" or Continue == "Yes" or Continue == "y" or Continue == "Y":
      AddingClasses = True
    if Continue == "NO" or Continue == "no" or Continue == "No" or Continue == "n" or Continue == "N":
      AddingClasses = False

  print()
  print(student, "\n")
  



############################# FOUR #####################################

def prob4():
  import time
  from StopWatch import StopWatch
  stopWatch = StopWatch()
  #stopWatch.returnTime()
  
    
    

  empty = 0
  stopWatch.start()
  for i in range(1,1000001):
    empty += i
    
  stopWatch.stop()
  print(f'Sum of loop: {empty}')
  print(f"Stop Time: {stopWatch.getEndTime()}")
  print(f"Elapsed Time: {stopWatch.getElapsed()}")

  stopWatch.start()
  print("Count Down!")
  for i in range(10,0, -1):
    print(i)
    time.sleep(1)
  print()
  stopWatch.stop()

  

  print(f"Start Time: {stopWatch.getStartTime()}")
  print(f"Elapsed Time: {stopWatch.getElapsed()}")
  print(f"Stop Time: {stopWatch.getEndTime()}")






#while 1+1 == 2:
#  print("yaba daba doo!")

################################# FIVE ##########################################

def prob5():
  import turtle
  from NEWLinearEquation import Line, LinearEquation

  

  window = turtle.Screen()

  line1 = Line(200, 200, 0, 0)
  line2 = Line(0, 200, 200, 0)
  

  line3 = Line(-250, 250, 0, 0)
  line4 = Line(-250, 0, 0, 250)

  line5 = Line(100, 0, 0, -100)
  line6 = Line(0, -10, 200, -200)

  line7 = Line(-100, 0, 0, -100)
  line8 = Line(-200, 0, 0, -200)

  lq1 = LinearEquation(line1, line2)
  lq1.drawGraph()
  lq1.drawVertex()

  lq2 = LinearEquation(line3, line4)
  lq2.drawVertex()

  lq3 = LinearEquation(line5, line6)
  lq3.drawVertex()

  lq4 = LinearEquation(line7, line8)
  lq4.drawVertex()

  line1.drawLine("blue")
  line2.drawLine("red")

  line3.drawLine("green")
  line4.drawLine("purple")

  line5.drawLine("green")
  line6.drawLine("blue")

  line7.drawLine("gold")
  line8.drawLine("red")

  print(line1)
  print(line2)
  print(line3)
  print(line4)
  print(line5)
  print(line6)
  print(line7)
  print(line8)
  print()
  print(f"Line 1 M: {line1.getM()}")
  print(f"Line 2 M: {line2.getM()}")
  print(f"Line 3 M: {line3.getM()}")
  print(f"Line 4 M: {line4.getM()}")
  print(f"Line 5 M: {line5.getM()}")
  print(f"Line 6 M: {line6.getM()}")
  print(f"Line 7 M: {line7.getM()}")
  print(f"Line 8 M: {line8.getM()}")
  print()
  print(f"Line 1 B: {line1.getB()}")
  print(f"Line 2 B: {line2.getB()}")
  print(f"Line 3 B: {line3.getB()}")
  print(f"Line 4 B: {line4.getB()}")
  print(f"Line 5 B: {line5.getB()}")
  print(f"Line 6 B: {line6.getB()}")
  print(f"Line 7 B: {line7.getB()}")
  print(f"Line 8 B: {line8.getB()}")

  
 

 

  window.mainloop()






prob1()
prob2()
prob3()
prob4()
prob5()