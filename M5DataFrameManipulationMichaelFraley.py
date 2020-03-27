import pandas as pd

def addASpace():
    return input()

Grade = {}
indexTestGrades = []

amountOfGrades = int(input("How many test would you like to enter => "))



for x in range(amountOfGrades):
    am = input("Enter the name of the test => ")
    indexTestGrades.append(am)
addASpace()
    
studentCount = int(input("How many students are in your class? => "))


for kids in range(studentCount):
    student = input("Enter the name of the student => ")
    Score = []
    for i in range(amountOfGrades):
        gr = input(f'Enter the grade of the student {student} for {indexTestGrades} => ')
        Score.append(gr)
    Grade.update({student: Score})
    addASpace()
grades = pd.DataFrame(Grade)
grades.index = indexTestGrades
print(grades)