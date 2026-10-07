# =  assigns:   put 20 into age
# == compares:  is age equal to 20?

age = 20
print(age == 20)    # True

# A str is never equal to an int. No error, just False.
pin = "4321"
print(pin == 4321)      # False
print(pin == "4321")    # True

# What to do instead: compare like with like.
print(pin == "4321")        # True   text with text (a PIN is text; keeps a leading zero)
print(int(pin) == 4321)     # True   number with number, converted before comparing
