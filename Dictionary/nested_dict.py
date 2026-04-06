student = {
    "name": "John",
    "age": 20,
    "marks": {
        "math": 90,
        "science": 85
    }
}

# Add key
student["grade"] = "A"

# Update value
student["age"] = 25

# Access value
print(student["name"])
print(student.get("age"))

# Access nested
print(student["marks"]["math"])

# Update nested
student["marks"]["math"] = 95

# Add nested
student["marks"]["english"] = 88

# Remove key
student.pop("grade")

# Remove nested
del student["marks"]["science"]

print(student)