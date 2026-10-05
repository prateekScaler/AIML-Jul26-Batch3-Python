# Why payment systems do not store money as a float.

print(0.1 + 0.2)          # 0.30000000000000004, not 0.3

# Floats are stored in binary, and many decimals cannot be stored exactly.
# So real payment systems keep money as an int in the smallest unit (paise).

price_paise = 29900       # 299 rupees, stored as 29900 paise
fee_paise = 10            # 10 paise
print(price_paise + fee_paise)   # 29910, exact

# Casting a float to an int cuts the decimal part off. It does not round.
print(int(99.9))          # 99
