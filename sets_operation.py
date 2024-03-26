# Part 2: Set Creation and Operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Adding an element to set1
set1.add(6)
print("After adding 6 to set1:", set1)

# Set union
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

# Set intersection
intersection_set = set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

# Set difference
difference_set = set1.difference(set2)
print("Difference between set1 and set2:", difference_set)

# Checking if set1 is a subset of set2
is_subset = set1.issubset(set2)
print("Is set1 a subset of set2?", is_subset)

# Removing an element from set2
set2.remove(6)
print("After removing 6 from set2:", set2)

# Part 3: Set Methods
# Popping an element from set1
popped_element = set1.pop()
print("Popped element from set1:", popped_element)

# Clearing set2
set2.clear()
print("set2 after clearing:", set2)

# Creating a copy of set1
set1_copy = set1.copy()
print("Copy of set1:", set1_copy)

# Part 4: Set Comprehensions
# Set of squares from 1 to 10
squares_set = {x**2 for x in range(1, 11)}
print("Set of squares from 1 to 10:", squares_set)

# Set of vowels in a string
string = "Hello, World!"
vowels_set = {char for char in string if char.lower() in 'aeiou'}
print("Set of vowels in the string:", vowels_set)

# Part 5: Application of Sets
# Sets are beneficial for removing duplicates and checking for membership efficiently.
# For example, in a list of email addresses, using a set can quickly identify unique addresses.
# Justification: Sets automatically remove duplicates, and membership testing is performed in constant time,
# making them efficient for such scenarios.
