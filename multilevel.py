#code by vedant kale
#multilevel
class rank:
    def classrank(self):
        c1=int(input("Enter your marks out of 100"))
        print("Your marks are:",c1)
class hod(rank):
    def h1(self):
        h2=input("Enter your hod name:")
        print("your hod name is ",h2)
class classteacher(hod):
    def cname(self):
        c2=input("Enter your class teacher name:")
        print("class teacher name is",c2)

obj1=classteacher()
obj1.classrank()
obj1.h1()
obj1.cname()