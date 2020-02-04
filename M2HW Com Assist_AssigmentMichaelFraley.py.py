import random


def MainMenu():
    print("1. Easy Mode")
    print("2. Hard Mode")
    print("3. Exit")
    selection = int(input("Enter Choice: "))
    if selection == 1:
        easymode()
    elif selection == 2:
        hardmode()
    elif selection == 3:
        exit
    else:
        print("Invalid choice. Enter 1-3: ")
        MainMenu()


def easymode():
    bool = True
    while bool == True:
        wrongValue = ["No, Keep Trying", "No, Please try again", "Wrong try once more"]
        rightValue = ["Very Good", "Nice Work", "Keep up the good work"]
        num1 = random.randint(1, 9)
        num2 = random.randint(1, 9)
        answer = int(input("What is " + str(num1) + " times " + str(num2) + "?: "))
        if (answer == num1 * num2):
            print(random.choice(rightValue))
            userContinue = input("would you like to do another problem? y/n: ")
            if userContinue == "y":
                easymode()
            elif userContinue == "n":
                bool = False
        else:
            print(random.choice(wrongValue))
            userContinue = input("would you like to do another problem? y/n: ")
            if userContinue == "y":
                easymode()
            elif userContinue == "n":
                bool = False


def hardmode():
    bool = True
    while bool == True:
        wrongValue = ["No, Keep Trying", "No, Please try again", "Wrong try once more"]
        rightValue = ["Very Good", "Nice Work", "Keep up the good work"]
        num1 = random.randint(10, 100)
        num2 = random.randint(10, 100)
        answer = int(input("What is " + str(num1) + " times " + str(num2) + "?: "))
        if (answer == num1 * num2):
            print(random.choice(rightValue))
            userContinue = input("would you like to do another problem? y/n: ")
            if userContinue == "y":
                hardmode()
            elif userContinue == "n":
                bool = False
        else:
            print(random.choice(wrongValue))
            userContinue = input("would you like to do another problem? y/n: ")
            if userContinue == "y":
                hardmode()
            elif userContinue == "n":
                bool = False


MainMenu()