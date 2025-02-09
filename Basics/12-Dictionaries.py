student = {"name": "Abhijeet", "age": 23, "course": "Python"}
print(student["name"])

student["age"] = 24
student["city"] = "Hazaribag"

print(student)

for key, value in student.items():
    print(key, ":", value)