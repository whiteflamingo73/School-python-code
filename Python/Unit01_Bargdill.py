###############################################################################
#     Name : Aaron Bargdill                 Date: 9/11/24                     #
#     Unit 1 Problem 1 Print Fun                                              #
#     Print the word fun to the screen with letters and print statements      #
###############################################################################



import math


#printing DHS in asci art for problem 1
print("Problem 1.")
print("I'm a student at:")
print("          ")
print("DDDD      HH     HH      SSSS")
print("DD  DD    HH     HH   SS     SS")
print("DD    DD  HH     HH     SS")
print("DD    DD  HHHHHHHHH      SS")
print("DD    DD  HH     HH       SS")
print("DD  DD    HH     HH   SS     SS")
print("DDDD      HH     HH     SSSS")

#Problem 2
#using order of operations to solve the division problem
print("           ")
print("Problem 2.")
print((58 * 42 - 35 * 55 - 11)/( 14 - 4))

#problem 3
#adding consecutive integers until getting to an answer of 45 
print("    ")
print("Problem 3.")
print(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9)

#problem 4
#figuring out the area of a circle with the radius of 13.86
print("    ")
print("Problem 4.")
print(math.pi * 13.86**2)

#problem 5
#The area of a rectangle with the side lengths of 4.5 and 7.5
print("    ")
print("Problem 5.")
print("Area:")
print(4.5 * 7.5)
print("Perimeter:")
print(4.5 + 4.5 + 7.5 + 7.5)

#problem 6
#trying to figure out the projected population growth of the US using birth rates, death rates, and imigration rates
#1 birth every 7 seconds(+)
#1 death every 13 seconds(-)
#1 new immigrant every 45 seconds(+)
#need to show population projection every year for the next 5 years
print("    ")
print("Problem 6.")
print("current population: 312032486")
seconds_per_year = (((60 * 60) * 24) * 365) 
birth_rate = str(seconds_per_year // 7)
death_rate = str(seconds_per_year // 13)
immigration_rate = str(seconds_per_year // 45)
current_population = (312032486)
population_gain = (4505142 + 700800 - 2425846) # birth rate + immigration rate - death rate
print("Birth s per year: " + birth_rate)
print("Deaths per year: " + death_rate)
print("Immigration rate per year: " + immigration_rate)
print("Population goes up per year by:")
print(population_gain)
print("US population at the end of the year:") #after each year the population drifts by 1 for each progressing year
# so I added the respective amount for each year to make up the difference
print(current_population + population_gain)
print("  ")
print("US population in two years:")
print((current_population + 1 + (population_gain * 2)))
print("  ")
print("US population in three years:")
print((current_population + 2 + (population_gain * 3)))
print("  ")
print("US population in four years:")
print((current_population + 3 + (population_gain * 4)))
print("  ")
print("US population in five years:")
print((current_population + 4 + (population_gain * 5)))
