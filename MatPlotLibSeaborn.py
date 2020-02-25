# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 10:25:31 2020

@author: Fraleym7700
"""

import matplotlib.pyplot as plt
import seaborn as sns

name = ["Corporate", "Finance", "Marketing"]
expenses = [15000, 20000, 25000]

plt.bar(name, expenses)
plt.title("Expendature")
plt.xlabel("Department")
plt.ylabel("Spending")

axes = sns.barplot(name, expenses)
axes.set_title("Expendature")
axes.set(xlabel = "Department", ylabel = "Spending")

plt.show()