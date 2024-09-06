# Create Tuple
# Tuples are similar to lists, but they are immutable, meaning that the values inside a tuple cannot be changed. Tuples are created using parentheses instead of square brackets.
my_tuple = (1, 2, 3, 4, 5)

# Access Tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3

# Update Tuple
updated_tuple = my_tuple + (6, 7)
print(updated_tuple)  # Output: (1, 2, 3, 4, 5, 6, 7)
# Remove elements from Tuple
#if we want to remove the elements from the tuple, we can convert the tuple to a list, remove the elements, and then convert the list back to a tuple. using slicing
removed_tuple = list(updated_tuple)
removed_tuple.remove(3)
removed_tuple.remove(5)
removed_tuple = tuple(removed_tuple)
print(removed_tuple)  # Output: (1, 2, 4, 6, 7)
# Delete Tuple
del my_tuple
# print(my_tuple)  # This will raise an error since the tuple no longer exists