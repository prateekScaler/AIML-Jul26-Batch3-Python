# Logical operators combine conditions.

age = 20
has_id = True
print(age >= 18 and has_id)    # True   and: both must be True

has_card = False
has_cash = True
print(has_card or has_cash)    # True   or: at least one must be True

is_raining = False
print(not is_raining)          # True   not: flips the value

# Comparisons create conditions. Logical operators combine them.
can_enter = age >= 18 and has_id
print(can_enter)               # True

# Other ways to write the same condition
can_enter = has_id and age >= 18             # same checks, other order
is_adult = age >= 18                         # name each check first
can_enter = is_adult and has_id
can_enter = not (age < 18 or not has_id)     # "not blocked" says the same thing
print(can_enter)                             # True
