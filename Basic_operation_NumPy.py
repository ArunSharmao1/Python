import numpy as np

# Task 1: Create a NumPy array arr1 with shape (3, 3) containing integers from 1 to 9
arr1 = np.arange(1, 10).reshape(3, 3)

# Task 2: Print the array arr1
print("Array arr1:")
print(arr1)

# Task 3: Create a NumPy array arr2 with shape (3, 3) containing random floating-point numbers between 0 and 1
arr2 = np.random.rand(3, 3)

# Task 4: Print the array arr2
print("\nArray arr2:")
print(arr2)

# Task 5: Perform element-wise addition, subtraction, multiplication, and division on arr1 and arr2, and print the results
print("\nElement-wise addition:")
print(arr1 + arr2)

print("\nElement-wise subtraction:")
print(arr1 - arr2)

print("\nElement-wise multiplication:")
print(arr1 * arr2)

print("\nElement-wise division:")
print(arr1 / arr2)

# Task 6: Compute the mean, median, and standard deviation of arr1, and print the results
print("\nMean of arr1:", np.mean(arr1))
print("Median of arr1:", np.median(arr1))
print("Standard deviation of arr1:", np.std(arr1))

# Task 7: Reshape arr1 into a 1D array and print the result
arr1_1d = arr1.flatten()
print("\nReshaped arr1 (1D):")
print(arr1_1d)

# Task 8: Create a new array arr3 by stacking arr1 and arr2 vertically
arr3 = np.vstack((arr1, arr2))

# Task 9: Print the shape of arr3
print("\nShape of arr3:", arr3.shape)
