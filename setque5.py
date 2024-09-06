
# Create an empty set
names_set = set()

# Add five new names to the set
names_set.add("Alice")
names_set.add("Bob")
names_set.add("Charlie")
names_set.add("David")
names_set.add("Eve")

# Modify one existing name
names_set.remove("Bob")
names_set.add("Ben")

# Delete two names
names_set.remove("Charlie")
names_set.remove("David")

# Print the final set
print(names_set)

