mylist = []
amountOfHours = int(input("Enter the amount of hours:"))
for x in range(amountOfHours):
    mylist.append(int(input()))
speed = int(input("Enter the speed you car is going: "))
total = 0
print("Hours \t DistanceTraveled")
for index, num in enumerate(mylist):
    result = num * speed
    mylist[index] = result
    total = total + result
    print(num, "\t", result)
    
print("Total\t",total)
#print(mylist)
