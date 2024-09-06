#default arguments
'''def average(a=9,b=7):
    print("The average is ",(a+b)/2)
average(4)

def name(fname, mname = "Pramod", lname = "Kale"):
    print("Hello,", fname, mname, lname)
name("vedant")'''

#variable length arguments: accessed by two methods as follows
#1.arbitary arguments
'''def average1(*num):#single can basically used for the arguments as in the form of tuples
    sum=0
    for i in num:
        sum=sum+i
    print("The average is: ",sum/ len(num))

average1(7,8,17)#arguments are in the form of the tuples'''

#keyword arbitary arguments:
"""def name(**name):#arguments in the form of the dictionary
    print("Hello,", name["fname"], name["mname"], name["lname"])

name(mname = "Pramod",  fname = "vedant",lname = "Kale")"""

#return statement
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)

c= average(4,5,6,9)
print(c)


