#here we are going to se list methods and manipulating it
l = [90,89,100,21,2,45,4,56,7,3,4,90]
#l.append(8)
#l.sort()
#l.sort(reverse=True)#sorting in the reverse
#l.reverse()#only reverses the string and doesnt sort
#print(l.index(45))#only returns the 1st occurence of that value
#print(l)
#print(l.count(90))

#copy method
#m =  l.copy()
#m[0]=0
#print("l is the list",l)
#print("m is the list",m)

#insert method
l.insert(0,99)
#extend method
m = [100,45,89,44,77,89,45]
#l.extend(m)#open list l and put the m list to the end of the l list
#concatenation of the two strings
k=l+m
#print(k)

#print(l)
counter=0
for i in l:
    print(counter,"",i)
    counter=counter+1