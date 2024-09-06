num1 = int(input("Enter the value of the num:"))

if(num1<0):
    print("The value is negative !!")
elif(num1>0):
    if(num1>=10):
        print("The number is between 1 - 10 ")
    elif(num1 >10 and num1 <20):
        print("The number is between 10 - 20 ")
    else:
        print("The number is gretor than 20")
else:
    print("The given number is zero !!") 