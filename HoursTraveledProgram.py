mylist = [3,6,9]
speed = 65
total = 0
print("Hours \t DistanceTraveled")
for index, num in enumerate(mylist):
    result = num * speed
    mylist[index] = result
    total += result
    print(num, "\t", result)
    
print("Total\t",total)
#print(mylist)
