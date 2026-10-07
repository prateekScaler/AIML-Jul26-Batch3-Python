# Why floats are not exact.
# In decimal, 1/3 never ends. Cut it to 0.33 and the pieces no longer add up to 1.
print(0.33 + 0.33 + 0.33)   # 0.99

# A computer counts in binary, and in binary 0.1 never ends either.
# So it is stored cut short, and the tiny error shows up when you add.
print(0.1 + 0.2)            # 0.30000000000000004
print(0.1 * 3)              # 0.30000000000000004

# This is why payment systems keep money as whole paise, not float rupees.
