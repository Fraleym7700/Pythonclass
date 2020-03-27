#MENU
#---------------------------------------
#1)	Create dictionary
#2)	Search for TLD
#3)	Add to dictionary
#4)	Update dictionary
#5)	Display dictionary content
#6)	Exit
#For choice 1. User is prompt to enter dictionary values
#For 2. User is to enter country name and TLD would be displayed
#For 3. Prompt user for country name and TLD and add to dictionary
#For 4. Prompt user to enter key and new TLD, update dictionary accordingly
#For 5. Display content in tabular format
#For 6. Terminate program
#5. After every operation, menu is to be displayed again until user chooses to terminate by entering 5.
def Menu():
  print("1)Create Dictionary\n2)Search for TLD\n3)Add to Dictinary\n4)Update Dictionary\n5)Display Dictionary\n6)Exit")

def CreateDictionary():
  return dict()

def SerachforTLD(**newDict):
  phrase = input("Enter the TLD you would to search for and we will tell you if you have it")
  if phrase in newDict:
    print("Yes,",phrase," is in the dictionary")
  else:
    print("No,",phrase," is not in the dictionary")

def AddToDictionary(**newDict):
  key = input("What would you like your key to be? ->")
  value = input("What would you like your value to be? ->")
  return newDict.update({key : value})

def UpdateDictionary(**newDict):
  key = input("What key would you like to update? ->")
  value = input("What would you like your value to be? ->")
  for key, value in newDict.items():
    newDict[key] = value
  return newDict

def DisplayDictionary(**newDict):  
  for x in newDict:
    newDict[x]



loop = "True"

while loop == "True":
  print(Menu())
  print()
  choice = input("Please enter an interger to continue")
  if choice == "1":
    newDict = CreateDictionary()
    print (newDict)
  elif choice == "2":
    SerachforTLD(**newDict)
  elif choice == "3":
   newDict = AddToDictionary(**newDict)
  elif choice == "4":
   newDict = UpdateDictionary(**newDict)
  elif choice == "5":
    DisplayDictionary(**newDict)
  elif choice == "6":
    loop = "False"


