#while loops in python
'''i=int(input("Enter the number :"))
while(i<=11):#it checks its condtion in every iteration
    i=int(input("Enter the number which is less than 10:"))
    print(i)
    i=i+1
print("Loop executed)'''
#in the above loop the while loop gets executed until the value of the i will be greator than 11

#decrementing the loop or we can say it is reverse loop
'''count=5
while(count>0):
    print(count)
    count=count-1'''

#while with else
'''count=5
while(count>0):
    print(count)
    count=count-1
else:
    print("I am inside the else part!!")'''

#do while loop in python and also called as the exit-controlled loop
'''
The most common technique to emulate a do-while loop in Python is to use 
an infinite while loop with a break statement wrapped in an if statement 
that checks a given condition and breaks the iteration if that condition
 becomes true
 do{
 
 }while(condition);c language syntax

'''
'''while True:
  number = int(input("Enter a positive number: "))
  print("The number is :",number)
  if not number > 0:
    print("The loop is exited!!")
    break'''
#tip press control + c to exit the infinite loops
#semi complex example
name1="vedant"
counter1=0
while True:
  word=input("Enter any word :")
  print("You entered string is:",word)
  counter1=counter1+1
  if(word==name1):
    print("Loop exited succesfully!!!")
    print("You entered string is:",word)
    break
  elif(word!=name1 and counter1>7):
    print("Loop exited succesfully!!")
    print("You entered string is:",word)
    break
  



