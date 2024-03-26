# Part 1: Tuple Creation and Access
my_tuple = (10, 20, 30, "hello", 3.14)
print("Second element of my_tuple:", my_tuple[1])
print("Last three elements of my_tuple:", my_tuple[-3:])

# Part 2: Tuple Concatenation and Repetition
tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
concatenated_tuple = tuple1 + tuple2
repeated_tuple = tuple1 * 3
print("Concatenated tuple:", concatenated_tuple)
print("Repeated tuple:", repeated_tuple)

# Part 3: Tuple Operations
print("Length of my_tuple:", len(my_tuple))
print("Is 30 present in my_tuple?", 30 in my_tuple)
fruit_tuple = ("apple", "banana", "cherry")
fruit1, fruit2, fruit3 = fruit_tuple
print("Tuple unpacking:", fruit1, fruit2, fruit3)

# Part 4: Tuple Methods
print("Number of occurrences of 10 in my_tuple:", my_tuple.count(10))
print("Index of 'hello' in my_tuple:", my_tuple.index("hello"))

# Part 5: Immutability of Tuples
try:
    my_tuple[0] = 100  # Attempting to modify an element of my_tuple
except TypeError as e:
    print("Error occurred:", e)
    print("Tuples are immutable and cannot be modified.")
