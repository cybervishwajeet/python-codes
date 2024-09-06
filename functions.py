#functions in python
def calculatethemean(a,b):
    mean=(a*b)/(a+b)
    print("The geometric mean is:",mean)

def greatororsmall(a,b):
    if(a>b):
        print("A is the greatest i.e.",a)
    elif(a==b):
        print("Both the numbers are equal!")
    else:
        print("B is the greatest number i.e.",b)

#empty functions
def islesser(a,b):
    pass


a = int(input("Enter the first number between 1 to 10:"))
b = int(input("Enter the second number between 1 to 10:"))
calculatethemean(a,b)
greatororsmall(a,b)
'''gmean = (a*b)/(a+b)
print(gmean)'''

'''These functions are defined and pre-coded in python. Some examples of
 built-in functions are as follows:

min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), 
set(), print(), etc
'''