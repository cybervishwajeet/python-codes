class sports:
    def Sports_name(self):
        fname=input("Enter the name:")
        sname=input("Enter the sports name which you like the most:")
        print("Student name",fname,"fav sports:",sname)

class Dept(sports):
    def departname(self):
        dname=input("Please enter your department name:")
        print("department name is :",dname)

obj1 = Dept()
obj1.Sports_name()
obj1.departname()