# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 10:04:44 2020

@author: Fraleym7700
"""

list1 = [num for num in range(1,1000)]
list2 = {num: num**2 for num in range (1,100)}
#Allows you to run through the list and multiply, easier to run through.
for x, y in list2.items():
    print(x,"\t", y)