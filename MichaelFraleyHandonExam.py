#Hands on Exam #1
#Your Name
#Date
#Loops and Functions

#Instructions
#Answer each task after the instructions given code should be short and to the point


#Task 1 # 5 points
#Rename this file with your name  ie cameronhandsonexam1
#
#write code to print your name

print("Michael Fraley") 


#Task 2 # 15 points
#Create a loop that displays the  following pattern
"""

*
***
*****
*******
*********

"""
NUM_STEPS = 5
for r in range(NUM_STEPS):
    print("*", end='')
    for c in range(r):
        print('**', end='')
    print(' ')

    


#Task 3 # 15 points
# Create a loop that asks user to enter sales generated, no limit to numbers entered
# numbers entered should be between 1 and 2000
# if user enters a value that is NOT within the defined range, notify user and prompt
# user to enter the sales amount again, hint: sentinals
# calculate total amount of sales entered . hint : running total
keep_going = "y"
while keep_going == "y":
    print(" ------------------------------------------------------------------------------------")
    print(" ------------------------------------------------------------------------------------")
    userChoice = int(input("    Welcome to the program \n     press 1 to enter your sales \n     press 2 to exit\n\n"))
    if userChoice == 1:
        totalAmount = 0
        print(" ------------------------------------------------------------------------------------")
        print(" ------------------------------------------------------------------------------------")
        salesGenerated = int(input("Enter the amount of Sales you generated: "))
        for x in range(salesGenerated):
            saleValue = float(input(""))
            if saleValue > 2000:
                print("Sorry Please Reenter the Value")
            totalAmount += saleValue
        print("The total of the sales are: ", totalAmount)
    elif userChoice == 2:
        keep_going = "n"
    else:
        exit()
#Task 4 # 10 points
# fill in the missing code in the code below
"""for ***:
    for ***:
        print("@")
    print()
"""
for x in range(7):
    for c in range(x):
        print("@")
    print("")
    
#replace the *** so that when the code is executed , it displays two rows , each containing
# seven @ symbols as shown below
# @@@@@@@
# @@@@@@@

NUM_STEPS = 2
for r in range(NUM_STEPS):
    print("@", end='')
    for c in range(7):
        print('@', end='')
    print(' ')
    
#Task 5 # 10 points
# correct the following code

"""
a = b = 7
print('a ='a,'/nb=',b)
"""


a = b = 7
print('a =',a, '\nb =',b)



# Task 6 # 15 points
# Create a function named get_sales
# add code created in task 3 to the created function
# run/call the function to test that it works

def get_sales():
    totalAmount = 0
    salesGenerated = int(input("Enter the amount of Sales you generated: "))
    for x in range(salesGenerated):
        saleValue = float(input(""))
        if saleValue > 2000:
            print("Sorry Please Reenter the Value")
        totalAmount = totalAmount + saleValue
    print("The total of the sales are: ", totalAmount)
get_sales()


#Task 7 # 15 points
# Create a function named get_random
# function is to generate two random numbers and display them 
# hint: import random module, make sure you call the function to verify that it displays to random numbers

import random
def get_random():
   num1 = random.randint(0,100)
   num2 = random.randint(0,100)
   print(num1, num2)
get_random()

# Task 8 # 15 points
# find out what's wrong with the following code 
# fix it and run it to prove it's working

"""
def cube(x):
    ''' Calculate the code of x.'''
    x**3
print('The cube for 2is',cube(2))

"""
def cube(x):
    cube = x**3
    return cube
print('The cube for 2 is',cube(2))




