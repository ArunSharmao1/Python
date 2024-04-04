# Step 1: Create a Dictionary
student_info = {
    "name": "Arun Sharma",
    "age": 18,
    "grade": "Graduate",
    "city": "Greater Noida"
}

# Step 2: Accessing Dictionary Elements
print("Name:", student_info["name"])
print("City:", student_info["city"])

# Step 3: Adding New Information
student_info["email"] = "sharmaarun22039@gmail.com"

# Step 4: Updating Information
student_info["age"] = 19

# Step 5: Deleting Information
del student_info["grade"]

# Step 6: Iterating Through Dictionary
print("Dictionary Contents:")
for key, value in student_info.items():
    print(key + ":", value)
