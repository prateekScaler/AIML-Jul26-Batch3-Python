# Cutting off decimals is not the same as rounding.
# In 1982-83 the Vancouver Stock Exchange index cut instead of rounding,
# thousands of times a day, and drifted from 1000 down to 524.811.
# Recalculated correctly it was 1098.892.

price = 99.9
print(int(price))     # 99   cuts
print(round(price))   # 100  rounds
