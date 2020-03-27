# Practice manipulating Data
# 3/14/2020
# CSC121 M4HW – Dictionary Manipulations
# Micahel Fraley


print("1)2)Create your list from the text book and check to see if the term 'Canada' and 'France' are in the dictionary")
print()

tlds = {'Canada': 'CA', 'United States': 'US', 'Mexico' : 'MX'}

if 'Canada' in tlds:
  print("Yes, 'Canada' is one of the keys in the tlds dictionary") 
if 'France' in tlds:
  print("Yes, 'France' is one of the keys in the tlds dictionary")
else:
  print("No, 'France' is one of the keys in the tlds dictionary")   
print()
print("3)Display your dictionary")
print('Country :\tTLD')
print('-----------------')
for x, y in tlds.items():
  print(x,":\t",y)
print()
print("4)Add the key-value pair 'Sweden' and 'sw'")
tlds["Sweden"] = "sw"
print('Country :\tTLD')
print('-----------------')
for x, y in tlds.items():
  print(x,":",y)
print()
print("5)Update the value sw to SE")
tlds["Sweden"] = "SE"
print('Country :\tTLD')
print('-----------------')
for x, y in tlds.items():
  print(x,":",y)
print()
print("6) Reverse the key and values")
reverseTlds = {value: key for key, value in tlds.items()}
print(reverseTlds)
print()
print("7) With the Results convert the country name to all caps ")
print()

tldsToUpper = dict((k.upper(), v.upper()) for k,v in tlds.items())
print('Country :\tTLD')
print('-----------------')
for x, y in tldsToUpper.items():
  print(x,":",y)
