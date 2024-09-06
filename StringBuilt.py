# String built-in functions example

# 1. len() - returns the length of a string
string = "vedant Kale!"
length = len(string)
print("Length of the string:", length)

# 2. upper() - converts a string to uppercase
uppercase = string.upper()
print("Uppercase string:", uppercase)

# 3. lower() - converts a string to lowercase
lowercase = string.lower()
print("Lowercase string:", lowercase)

# 4. capitalize() - capitalizes the first character of a string
capitalized = string.capitalize()
print("Capitalized string:", capitalized)

# 5. count() - returns the number of occurrences of a substring in a string
count = string.count("e")
print("Count of 'o':", count)

# 6. find() - returns the index of the first occurrence of a substring in a string
index = string.find("Kale")
print("Index of 'World':", index)

# 7. replace() - replaces all occurrences of a substring with another substring
replaced = string.replace("Dog", "Cat")
print("Replaced string:", replaced)

# 8. split() - splits a string into a list of substrings based on a delimiter
split_list = string.split(",")
print("Split list:", split_list)

# 9. isalpha() - checks if all characters in a string are alphabetic
is_alpha = string.isalpha()
print("Is alphabetic:", is_alpha)

# 10. isnumeric() - checks if all characters in a string are numeric
is_numeric = string.isnumeric()
print("Is numeric:", is_numeric)