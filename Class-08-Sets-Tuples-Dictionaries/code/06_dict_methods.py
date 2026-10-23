student = {"name": "Rajani", "age": 20}

print(student.keys())
print(student.values())
print(student.items())

student.update({"age": 22, "grade": "A"})
print(student)

removed = student.pop("grade")
print(removed)
print(student)
