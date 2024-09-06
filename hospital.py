#program by vedant kale
'''name1= input("Enter the name of the patient")
print("Name of the Patient:",name1)'''

for i in range(1,15,1):
    print("Good Morning All!!")
    str1=input("Do you want to enroll next Patient?\nType (y/n): ")
    if(str1=='y'):
        str2=input("Enter the name of the Patient:")
        print("Patient name:",str2)
        print("Patient number",i,"please enter in the ward")
        print("New patient addmitted!")
    elif(str1=='n'):
        print("A call from doctor to all patient!!\n All the please come on next day because todays entries are full!!\nSorry for inconvience! ")
        break
    else:
        print("Please enter a valid number!! or a call")
