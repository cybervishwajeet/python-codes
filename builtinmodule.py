import keyword
import math
import numbers
import operator


# Using the keyword module
print(keyword.iskeyword('if'))  # Output: True
print(keyword.iskeyword('hello'))  # Output: False

# Using the math module
print(math.sqrt(16))  # Output: 4.0
print(math.pi)  # Output: 3.141592653589793

# Using the numbers module
print(numbers.Real.__subclasses__())  # Output: [<class 'numbers.Complex'>, <class 'numbers.Rational'>]

# Using the operator module
a = 5
b = 3
print(operator.add(a, b))  # Output: 8
print(operator.mul(a, b))  # Output: 15

# Get the list of keywords
keywords = keyword.kwlist

# Print each keyword
for kw in keywords:
    print(kw)
