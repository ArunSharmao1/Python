# Task 1: Print Even Numbers
print("Even numbers between 1 and 20:")
for num in range(1, 21):  # Loop through numbers from 1 to 20
    if num % 2 == 0:  # Check if the number is even
        print(num)

# Task 2: Sum of Odd Numbers
sum_odd = 0
num = 1
while num <= 50:  # Loop until reaching 50
    if num % 2 != 0:  # Check if the number is odd
        sum_odd += num
    num += 1
print("Sum of odd numbers between 1 and 50:", sum_odd)

# Task 3: Multiplication Table
number = int(input("Enter a number to print its multiplication table: "))
print("Multiplication table for", number, ":")
for i in range(1, 11):  # Loop through numbers from 1 to 10
    print(number, "x", i, "=", number * i)
