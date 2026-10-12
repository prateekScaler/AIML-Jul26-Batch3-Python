# A loop inside a loop: the inner loop runs fully for each outer pass.
for branch in range(3):
    for counter in range(2):
        print(branch, counter)

# Nested loops draw grids. end=" " keeps the stars on one line.
for row in range(3):
    for column in range(3):
        print("*", end=" ")
    print()

# The inner range may use the outer variable: a growing triangle.
for row in range(1, 4):
    for column in range(row):
        print("₹", end=" ")
    print()
