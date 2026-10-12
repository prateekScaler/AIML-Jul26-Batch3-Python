# Mini project: print 1 up to n and label each number even or odd.
# range stops before its end value, so the stop is n + 1.
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i, "- Even")
    else:
        print(i, "- Odd")
