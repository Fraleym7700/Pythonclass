from collections import collections


numbersOfEmployees = int(input('How many employees do you have?: '))
total = 0
for x in range(numbersOfEmployees):
 hoursWorked = int(input('How many hours did you work?: '))
 payRate = int(input('Your pay rate?: '))
 employeesName = input('What is your full name?: ')
 employeeSalary = hoursWorked * payRate
 total += employeeSalary
 a =[hoursWorked, payRate, employeesName, employeeSalary]
 a += a

 
 print('------------------------------------------------')
 print('Your hours worked is: ', hoursWorked)
 print('Your pay rate is: ', payRate)
 print('Your Full Name is: ', employeesName)
 print('Your Salary is: ', employeeSalary)
 print('------------------------------------------------')
print("-------------------------------------------------")
print('The total of salaries are: ', total)
print(a)