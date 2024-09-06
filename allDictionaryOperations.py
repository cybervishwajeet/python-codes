# Create Dictionary
# Dictionaries are collections of key-value pairs. Dictionaries are created using curly braces and colons.
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Access Dictionary elements
print(my_dict['name'])  # Output: John
print(my_dict.get('age'))  # Output: 25

# Update Dictionary
my_dict['age'] = 26
my_dict['city'] = 'San Francisco'
print(my_dict)  # Output: {'name': 'John', 'age': 26, 'city': 'San Francisco'}

# Delete Dictionary
del my_dict['age']
print(my_dict)  # Output: {'name': 'John', 'city': 'San Francisco'}

# Looping through Dictionary
for key, value in my_dict.items():
    print(key, value)