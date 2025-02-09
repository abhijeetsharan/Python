student = {
    "name": "Abhijeet",
    "age": 25,
    "course": "Computer Science"
}

print(student)

# Accessing Dictionary Values
print(student["name"])
print(student.get("age"))

# Adding & Updating Elements
student["city"] = "Hazaribag"
student["age"] = 24

print(student)

# Removing Elements
student.pop("city")
print(student)

del student["course"]
print(student)

student.clear()
print(student)