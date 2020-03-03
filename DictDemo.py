thisdict = {
  "Object1": 1**2,
  "Object2": 2**2,
  "Object3": 3**2,
  "Object4": 4**2,
  "Object5": 5**2
}
print("Num\t\tSqr")
for x, y in thisdict.items():
  print(x,"\t", y)



for x in thisdict:
  print(thisdict[x])
print()
  
for x in thisdict:
  print(x)
print()
if "Object1" in thisdict:
  print("Yes, 'Object1' is one of the keys in the thisdict dictionary")
print()
thisdict["object6"] = 6**2
for x, y in thisdict.items():
  print(x,"\t", y)
print()
print(len(thisdict))
print()
thisdict.pop("Object3")
for x, y in thisdict.items():
  print(x,"\t", y)
del thisdict["Object2"]
print()
for x, y in thisdict.items():
  print(x,"\t", y)
print()
thisdict.popitem()
for x, y in thisdict.items():
  print(x,"\t", y)
  