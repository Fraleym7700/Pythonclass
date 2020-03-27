# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 19:40:33 2020

@author: Fraley
"""
import numpy as np
import pandas as pd
def mainMenu():
    return "1.Create 3-by-3 Array\n2.Display Squared value\n3.Add 4 to each Element\n4.Multipy Elements by 6\n5.Exit"


    
def askuserForInput():
    a = int(input("Enter an interger:"))
    return a

def create3by3Array():
    num1 = askuserForInput()
    num2 = askuserForInput()
    num3 = askuserForInput()
    num4 = askuserForInput()
    num5 = askuserForInput()
    num6 = askuserForInput()
    num7 = askuserForInput()
    num8 = askuserForInput()
    num9 = askuserForInput()
    arr = np.array([[num1,num2,num3],
          [num4,num5,num6],
          [num7,num8,num9]])
    for row in arr:
        for column in row:
            print(column, end=' ')
        print()
    return arr
    

#def arrayElementSquaredValue():
#def add4toEachElementsinArray():

#def MuliplyArrayElementsby6():
loop = "true";
while loop == "true":
    print(mainMenu())
    choice = input("=> ")
    if choice == "1":
      arr = create3by3Array()
    elif choice == "2":
        print(arr ** 2 )
    elif choice == "3":
        print(arr + 4)
    elif choice == "4":
        print(arr * 6)
    elif choice == "5":
        loop = "false"
    else:
        print("Please choose from the choices above")
        print()