# Create Set
# Sets are unordered collections of unique elements. Sets are created using curly braces instead of square brackets.
my_set = {1, 2, 3, 4, 5}

# Access Set elements
for element in my_set:
    print(element)

# Update Set
my_set.add(6)
my_set.update([7, 8, 9])

# Delete Set
my_set.remove(3)
my_set.discard(4)
my_set.clear()

print(my_set)  # Output: set()