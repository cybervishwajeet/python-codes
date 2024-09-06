#matchcase program
x = int(input("Enter the value for the x:"))

match x:
    case 0:
        print("X is zero")
    case 4:
        print("Case is four")
    case _ if x==90:
        print(x,"is 90")
    case _ if x!=90:
        print(x,"is not equal to 90")
    case _:#this is how we can define the default from the match case
        print("The value of the",x)
