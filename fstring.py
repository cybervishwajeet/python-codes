#fstrings in the python
#letter ="hey my name is {} and I am from {}"
country="India"
name="Vedant"
#print(letter.format(name,country))
letter ="hey my name is {1} and I am from {0}"
#print(letter.format(country,name))

print(f"Hey my name is {name} and I am from {country}")

txt="For only {} dollars!"#another good example
#print(txt.format(price=49.00000454))

#by fstring now 
price=49.4545
txt=f"For only {price:.2f} dollars!"
print(txt)

print(f"Hey my name is {{name}} and I am from {country}")