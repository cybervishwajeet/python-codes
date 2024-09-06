import random

# Create an empty set
number_set = set()

# Generate 10 random numbers in the range 15 to 45
for _ in range(11):
    number = random.randint(15, 45)
    number_set.add(number)

print("The Number Set Before Operation:",number_set)

# Count how many numbers are less than 30
count_less_than_30 = sum(1 for num in number_set if num < 30)

# Delete numbers greater than 35
number_set = {num for num in number_set if num <= 35}

print("Number set:", number_set)
print("Count of numbers less than 30:", count_less_than_30)
