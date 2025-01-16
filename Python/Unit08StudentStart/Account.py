import time

class Account:
  def __init__(self, name="no name", savings=0, checking=0):
    self.__idd = (int)(time.time())
    self.__name = name
    self.__checking = checking
    self.__savings = savings
  
  def getID(self):
    return self.__idd
  
  def getName(self):
    return self.__name
  
  def getChecking(self):
    return self.__checking
  
  def getSavings(self):
    return self.__savings
  
  def checkingDeposit(self, deposit):
    if deposit > 0:
      self.__checking = self.__checking + deposit
      return self.__checking
    else:
      print("Account Deposit invalid")
      
  
  def checkingWithdrawl(self, withdrawl):
    if withdrawl > 0:
      if withdrawl > self.__checking:
        if withdrawl < self.__checking + self.__savings:
          withdrawl = withdrawl - self.__checking
          self.__checking = 0
          self.__savings = self.__savings - withdrawl
          return self.__checking, self.__savings
        if withdrawl > self.__checking + self.__savings:
          print("Withdrawl amount is too high")
      else:
        self.__checking = self.__checking - withdrawl
        return self.__checking
    else:
      print("Withdrawl amount invalid")
  
  def savingsDeposit(self, deposit):
    if deposit > 0:
      self.__savings = self.__savings + deposit
      return self.__savings
    else:
      print("Account Deposit invalid")
  
  def savingsWithdrawl(self, withdrawl):
    if withdrawl > 0:
      if withdrawl > self.__savings:
        print("Withdrawl amount is too high")
      else:
        self.__savings = self.__savings - withdrawl
        return self.__checking
    else:
      print("Withdrawl amount invalid")

      
  
  





  def __str__(self):
    return "Account ID: " + str(self.__idd) + " | Account Name: " + str(self.__name) + "\nChecking Balance: " + str(self.__checking) + " | Savings Balance: " + str(self.__savings) + " | Total Balance: " + str(self.__checking +self.__savings) + "\n"

