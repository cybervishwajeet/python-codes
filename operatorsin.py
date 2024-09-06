'''
Logical operators:  and,or,not
'''
print("And:",89>8 and 98>89)
print("Or:",89>98 or 98>89)
print("Or:",not(89>98 or 98>89))#changes the output from true to the false and false to the true

"""
Identity operators: is and is not

"""
#this are mainly used in the lists data type
x = ["vedant","Kale"]
y= ["Students","Gods"]
Q= ["vedant","Kale"]
z=x

print("X is Z",x is z)
print("X is Q", x is Q)#returns false because x is not the same object as of q , even if they have same contents
print("X == Y",x==y)#this is false
print("X == Q",x==Q)#this comparison returns True because x is equal to Q

print("X is not z:",x is not z)
print("X is not Q:",x is not Q)
print("X != Q:",x != Q)#to demonstrate the difference betweeen "is not" and "!=": this comparison returns False because x is equal to Q

'''
Membership operator: in and not in

'''
x = ["Aishwarya","Kale"]

print("Kale in x","kale"in x)
print("Pramod in x","Pramod"not in x)

