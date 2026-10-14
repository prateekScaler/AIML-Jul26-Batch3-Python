# Validation helpers: small functions that answer yes or no.
# Name them is_..., return a bool, check inputs at the door.
saved_pin = "4321"

def is_valid_amount(amount):
    return amount > 0 and amount <= 100000

def is_valid_pin(pin):
    return pin == saved_pin

print(is_valid_amount(600), is_valid_amount(-5), is_valid_amount(0))
print(is_valid_pin("4321"), is_valid_pin("1111"))
