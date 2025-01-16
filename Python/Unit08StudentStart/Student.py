import datetime

now = datetime.datetime.now()

class Student:
  def __init__(self,name="Unknown",grade=now.year,town="Unknown", classes = list(), scores = list()):
    self.__name = name
    self.__gradYear = grade
    self.__town = town
    self.__classes = classes
    self.__scores = scores

  
  
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
