age = int(input("Enter the age of the Voter:"))

if(age<18):
    print("You're not eligible for voting")
elif(age==0):
    print("Please enter a valid input!!")
else:
    print("you're eligible for voting!!!")
    