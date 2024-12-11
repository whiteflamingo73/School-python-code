############################################################
# Name : Aaron Bargdill Date: 12/3/24                      #
# Unit 7 Problems                                          #
# Count Digits, Smallest index of list, List shuffle       #
# Revise selection sort, bubble sort, merge sort           #
# Locker Problem, Turtle hangman                           #
############################################################

import turtle, random

#Problem 1: 
print("Promblem 1: Count of Digits")
print()
#just a variable to generate a random number from0-9
randomNum = random.randint(0,9)
#creating an empty list
randomList = []
#These are counters and will be used to keep track of each number
numof9 = 0
numof8 = 0
numof7 = 0
numof6 = 0
numof5 = 0
numof4 = 0
numof3 = 0
numof2 = 0
numof1 = 0
numof0 = 0
#adds a random number to the list a thousand times
for i in range(1000):
    randomList.append(random.randint(0,9))
#just here so I know it's working
#print(randomList)
#This is counting each digit in the list and won't stop until it's gone through the entire list
for number in randomList:
    if number == 0:
        numof0 += 1
    if number == 1:
        numof1 += 1
    if number == 2:
        numof2 += 1
    if number == 3:
        numof3 += 1
    if number == 4:
        numof4 += 1
    if number == 5:
        numof5 += 1
    if number == 6:
        numof6 += 1
    if number == 7:
        numof7 +=1
    if number == 8:
        numof8 += 1
    if number == 9:
        numof9 += 1

print("There are", numof0, "0's in the list")
print("There are", numof1, "1's in the list")
print("There are", numof2, "2's in the list")
print("There are",numof3, "3's in the list")
print("There are",numof4, "4's in the list")
print("There are",numof5, "5's in the list")
print("There are",numof6, "6's in the list")
print("There are",numof7, "7's in the list")
print("There are",numof8, "8's in the list")
print("There are",numof9, "9's in the list")

#Problem 2: Smallest Index
print()
print("Problem 2: Smallest Index")
print()
problem_2_list = []
def indexOfSmallestEllements(lst):
    for i in range(15):
        lst.append(random.randint(0,100))
    
    smallest = lst[0]
    for num in lst:
        for num in lst:
            if num < smallest:
                smallest = num
    
    index = lst.index(smallest)
    print("The smallest number in the list is", smallest)
    print("The smallest number is at the index position of:", index)
    return lst


print(indexOfSmallestEllements(problem_2_list))

#Problem 3: List Shuffle
print()
print("Problem 3: List Shuffle")
print()

myList = []
for i in range(10):
    myList.append(random.randint(0,100))

print(f"List of 10 random numbers from 0-100: {myList}")

#sorting the list
myList.sort()
print(f'The sorted list is: {myList}')


def shuffle(lst):
    newList = []
    for num in myList:
        amount = len(myList)
        num = (random.sample(lst, amount)) #num becomes the index, but we have to return the value from that position
        lst = num
        #need to append the random number being chosen to the new list
        return num
    return newList

newList = shuffle(myList)
print(f'The reshuffled list is: {newList}')


#Problem 4: Revise Selection Sort
print()
print("Problem 4: Revise Selection Sort")
print()

#sorts list
#starts at beginning of list
#finds smallest number in list and swaps with first item
#next smallest is swapped with next index in list
def selectionSortsm(lst):
  swaps = 0  #swaps counts how many times numbers were swapped to get the list in order
  for i in range(len(lst)):
    # Find the minimum in the lst[i : len(lst)]
    currentMin = lst[i]
    currentMinIndex = i
    
    #looks to see if there is a smaller number in the list and sets that to the smallest if it finds it
    for j in range(i + 1, len(lst)):
      if currentMin > lst[j]:
        currentMin = lst[j]
        currentMinIndex = j
    
    # Swap lst[i] with lst[currentMinIndex] if necessary
    if currentMinIndex != i:
      lst[currentMinIndex] = lst[i]
      lst[i] = currentMin
      swaps += 1
  print("Swaps", swaps)


"""Largest to Smallest"""

def selectionSortlg(lst):
  swaps = 0  #swaps counts how many times numbers were swapped to get the list in order
  for i in range(len(lst) - 1, -1):
    # Find the minimum in the lst[i : len(lst)]
    currentMin = lst[i]
    currentMinIndex = i
    #looks to see if there is a smaller number in the list and sets that to the smallest if it finds it
    for j in range(i -1, len(lst)):
      if currentMin > lst[j]:
        currentMin = lst[j]
        currentMinIndex = j
    # Swap lst[i] with lst[currentMinIndex] if necessary
    if currentMinIndex != i:
      lst[currentMinIndex] = lst[i]
      lst[i] = currentMin
      swaps += 1
  print("Swaps", swaps)





"create lists and sort with functions"


OrderList = []
for i in range(10):
    OrderList.append(random.randint(0,100))

OrderList2 = OrderList.copy()

selectionSortsm(OrderList)
print(OrderList)
print()

selectionSortlg(OrderList2)
print(OrderList2)