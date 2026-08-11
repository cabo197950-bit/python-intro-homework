student = {
    "name": "Tina",
    "grade": 95,
    "subjects": ["Python", "Data", "Web"]
}

for key, value in student.items():
    print(key, ":", value)

student["graduated"] = False

print("Updated dictionary:")
print(student)