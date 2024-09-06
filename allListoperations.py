# Create List
my_list = [1, 2, 3, 4, 5]

# Access List
print("Elements in the list:")
for item in my_list:
    print(item)

# Update List (Add Item)
my_list.append(6)
print("List after adding an item:", my_list)

# Update List (Remove Item)
my_list.remove(3)
print("List after removing an item:", my_list)

# Delete List
del my_list
print("List deleted.")