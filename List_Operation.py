# Part 1 Basic Operations with Lists

# Task 1
numbers = [1, 2, 3, 4, 5]
print("Original list:", numbers)
print("Length of the list:", len(numbers))
print("First element of the list:", numbers[0])
print("Last element of the list:", numbers[-1])

# Task 2
print("\nPerforming operations:")
numbers.append(6)
print("After appending 6:", numbers)
numbers.insert(0, 0)
print("After inserting 0 at the beginning:", numbers)
numbers.pop()
print("After removing the last element:", numbers)
numbers[1] = 10
print("After changing the second element to 10:", numbers)
numbers.reverse()
print("After reversing the list:", numbers)

# Part 2: List Methods

# Explanation of list methods
"""
- append(): Adds an element to the end of the list.
- insert(): Inserts an element at a specified position in the list.
- pop(): Removes and returns the last element of the list.
- index(): Returns the index of the first occurrence of a specified value.
- count(): Returns the number of occurrences of a specified value in the list.
- sort(): Sorts the list in ascending order.
- reverse(): Reverses the order of elements in the list.
"""

# Example demonstrating the usage of each method
print("\nDemonstrating list methods:")
example_list = [3, 1, 4, 1, 5, 9, 2, 6]

example_list.append(7)
print("After appending 7:", example_list)

example_list.insert(2, 0)
print("After inserting 0 at index 2:", example_list)

popped_element = example_list.pop()
print("Popped element (last):", popped_element)
print("List after pop:", example_list)

index_of_5 = example_list.index(5)
print("Index of 5:", index_of_5)

count_of_1 = example_list.count(1)
print("Count of 1:", count_of_1)

example_list.sort()
print("Sorted list:", example_list)

example_list.reverse()
print("Reversed list:", example_list)
