

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




prob1()


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



prob2()