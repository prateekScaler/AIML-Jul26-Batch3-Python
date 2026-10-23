# A dictionary looks things up by name, not by position.
student = {"name": "Rajani", "age": 20, "course": "AIML"}
print(student["name"])
print(student["age"])

# Update an existing key, add a new key.
student["age"] = 21
student["city"] = "Pune"
print(student)

# get: safe lookup. Square brackets: KeyError when the key is missing.
print(student.get("age"))
print(student.get("grade"))
print(student.get("grade", "Not assigned"))
# print(student["grade"])    # KeyError: 'grade'
