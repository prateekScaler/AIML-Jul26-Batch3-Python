# range: start is included, stop is excluded, step is optional.
print("range(5):")
for i in range(5):
    print(i)

print("range(1, 6):")
for token in range(1, 6):
    print("Token", token)

print("range(2, 11, 2):")
for i in range(2, 11, 2):
    print(i)

print("range(10, 0, -1):")
for sec in range(10, 0, -1):
    print("OTP expires in", sec)

print("range(10, 0) with no step prints nothing:")
for sec in range(10, 0):
    print("OTP expires in", sec)
