#strings are immutable
a="!!vedant!!!!!!!"
print("Length of the string is:",len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))#it does not trails the leading characters which are for the stripping

print(a.replace("vedant","John"))

blogheading="welcome to home"
print(blogheading.capitalize())

str1="Welcome to the console!!!"
print(str1.center(50))
print(str1.endswith("!!"))

str3= "abababchhadbhsa"
print(str3.count("a"))

#endswith complex example
print("Endswith example",str1.endswith("to",4, 10))

#find method
str1="He's name is Dan .He is an honest Man."
print(str1.find("is"))#only for 1st occurence


#for the alphanumeric charactristics
str1="WelcomeToConsole"
print("isalnum:",str1.isalnum())
print("isapha:",str1.isalpha())
print("islower:",str1.islower())
print("isprintable: ",str1.isprintable())

str1="     "
print(str1.isspace())

str1="Vedant kale is a stduent"
print(str1.startswith("Vedant"))
#to replace uppercase with the lower case
print(str1.swapcase())



