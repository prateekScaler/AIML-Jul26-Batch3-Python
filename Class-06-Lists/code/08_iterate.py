# Walk through a list with for. Use range(len(...)) when you also need the position.
students = ["Hitender", "Parvatha", "Shubhodip", "Akash"]

for student in students:
    print(student)

for i in range(len(students)):
    print(i, students[i])

scores = [35, 72, 45, 90, 28]
for score in scores:
    if score >= 40:
        print(score, "Pass")
    else:
        print(score, "Fail")
