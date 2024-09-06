#code by vedant kale
#multiple
class sports:
    def Sports_name(self):
        fname=input("Enter the name:")
        sname=input("Enter the sports name which you like the most:")
        print("Student name",fname,"fav sports:",sname)
class Division:
    def high(self):
        high1=input("Enter your Highest score in that sports:")
        div1=input("Enter your division:")
        print("Student div is:",div1,"and High score in sports is:",high1)
class Dept(sports,Division):
    def departname(self):
        dname=input("Please enter your department name:")
        print("department name is :",dname)

obj1 = Dept()
obj1.Sports_name()
obj1.departname()
obj1.high()