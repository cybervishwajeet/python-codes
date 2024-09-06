#lists in python
lists1=["vedant",3,"kk",True,"GPP",6,7,5,2,"Abhinav",6,9,0,67,False]
'''print(lists1)
print(lists1[0])
print(lists1[2])'''
#print(lists1[-3])
#print('vedant'in lists1)
#another method is
'''if "GPP" in lists1:
    print("Yes")
else:
    print("No")'''

#print(lists1[0:])
#print(lists1[0:10:2])#here 2 is the jump index

#list comprehension
#lst = [i for i in range(4)]
#print(lst)
#another expression
lst =[i for i in range(12) if (i%2)==0]
print(lst)