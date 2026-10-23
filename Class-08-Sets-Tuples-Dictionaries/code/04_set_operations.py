# Set operations: the same ideas as groups in maths.
python_students = {"Praveen", "Rahul", "Vamsi"}
sql_students = {"Rahul", "Vamsi", "Akshay"}

print(python_students | sql_students)    # union: in either
print(python_students & sql_students)    # intersection: in both
print(python_students - sql_students)    # difference: only in Python
print(python_students ^ sql_students)    # symmetric difference: in exactly one

# Membership
print("Rahul" in python_students)
print("Akshay" in python_students)
