# Create dictionary
student = {
    "name": "John",
    "age": 20,
    "marks": 85
}

print("Original Dictionary:", student)

student["place"] = "Kerala"
print("After adding place:", student)
# get()
print("Name:", student.get("name"))
print("Grade:", student.get("grade", "Not Found"))

# keys(), values(), items()
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# update()
student.update({"age": 21})
student.update({"grade": "A"})
print("After update:", student)

# setdefault()
student.setdefault("city", "Delhi")
print("After setdefault:", student)

# copy()
copy_student = student.copy()
print("Copied Dictionary:", copy_student)

# pop()
student.pop("age")
print("After pop:", student)

# popitem()
student.popitem()
print("After popitem:", student)

# Looping
print("Looping:")
for key, value in student.items():
    print(key, ":", value)

# fromkeys()
keys = ["x", "y", "z"]
new_dict = dict.fromkeys(keys, 0)
print("Fromkeys dict:", new_dict)

# clear()
student.clear()
print("After clear:", student)

# Iterating over nested dictionary
for key, value in student.items():
    if isinstance(value, dict):
        for sub_key, sub_value in value.items():
            print(sub_key, sub_value)
    else:
        print(key, value)