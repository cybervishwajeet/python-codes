#creating a list
names=['Anil','Amol','Aditya','Avi','Alka']
print(names)

#inserting the anuj before the aditya
names.insert(2,'Anuj')
print(names)

#appending name vedant
names.append('Vedant')
print(names)

#Deleting the name avi
names.remove('Avi')
print(names)

#replacing anil with anil kumar
names[0]='Anil Kumar'
print(names)

#sorting the list
names.sort()
print(names)

#reversing the list
names.reverse()
print(names)
