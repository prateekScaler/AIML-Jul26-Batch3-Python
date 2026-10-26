# Q3. Pattern printing and prime hunter (Class 4)

# (a) a right-aligned pyramid
n = int(input("n: "))
for row in range(1, n + 1):
    spaces = "  " * (n - row)
    numbers = ""
    for k in range(1, row + 1):
        numbers += str(k) + " "
    print(spaces + numbers.rstrip())

# (b) primes in a range
start = int(input("start: "))
end = int(input("end: "))
count = 0
for number in range(start, end + 1):
    if number < 2:
        continue
    is_prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(number, end=" ")
        count += 1
print()
print("Primes found:", count)

# (c) numbers until 0
total = 0
entered = 0
while True:
    value = int(input("Number (0 to stop): "))
    if value == 0:
        break
    total += value
    entered += 1
if entered > 0:
    print(f"Sum {total}, average {total / entered}")
else:
    print("No numbers entered.")
