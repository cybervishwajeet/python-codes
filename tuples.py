#tuples and its methods
#tup =(1,2,3,4,5,4,"green","vedant kale",True,float)
#print(type(tup))
#print(len(tup))
#tup[0]=10 tuple is immutable
#print(tup[0])
#print(tup[7])

#tup2=tup[0:len(tup)]
#print(tup2)
#print(tup2 is tup)#retruns true

#Range of index
#Tuple[start : end : jumpIndex]
#print(tup[::2])printing the alternative indexes
countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)  #here the tuple is converted into the lists for manupulation
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
#temp[2] = "Finland"         #change item
#countries = tuple(temp) #here again the list is converted into the tuple
#print(countries)

countries2 = ("Vietnam", "India", "China")
#tup3=countries+countries2
#print("Tup3 is",tup3)
#
#couting the elements
#c1 = countries.count('Spain')
#print(c1)

#tuple.index(element, start, end)
Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.index(3,0,len(Tuple1))
print('First occurrence of 3 is', res)