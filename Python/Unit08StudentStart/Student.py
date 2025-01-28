import datetime

now = datetime.datetime.now()

class Student:
  def __init__(self,name="Unknown",grade=now.year,town="Unknown", classes = list(), scores = list()):
    self.__name = name
    self.__gradYear = grade
    self.__town = town
    self.__classes = classes
    self.__scores = scores

  
  
  
  def setName(self):
    self.__name = str(input("What's your name? "))

  def getName(self):
    return self.__name
  
  
  def setGradYear(self, studentGrade):
    self.__gradYear = studentGrade

  def getGradYear(self):
    return self.__gradYear

  def getTown(self):
    return self.__town
  
  def setTown(self, studentTown):
    self.__town = studentTown

  def addClass(self, aclass, score):
    self.__classes.append(aclass)

  
    self.__scores.append(score)
  
  
  def printClasses(self):
    temp = ""
    avg = 0
    for x in range(len(self.__classes)):
      temp += self.__classes[x] + " - " + str(self.__scores[x]) + "\n"
      avg += int(self.__scores[x])
    
    avg /= len(self.__scores)
    temp += "Average = " + str(avg)
    return temp



  def __str__(self):
    return "Name: "+ self.__name + " | Grad Year: " + str(self.__gradYear) + " | Town: " + self.__town + "\nClasses:\n" + self.printClasses()
