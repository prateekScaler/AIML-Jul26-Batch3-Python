# Conditions built with and, or, not
balance = 1000
amount = 400
pin_correct = True

if balance >= amount and pin_correct:      # both must be True
    print("Payment successful")
else:
    print("Payment failed")

has_upi_pin = False
has_fingerprint = True
if has_upi_pin or has_fingerprint:         # at least one must be True
    print("Authorised")

is_frozen = False
if not is_frozen:                          # not flips the value
    print("Account active. Proceed.")

# A classic trap: this is always True, because "card" alone counts as True
mode = "cash"
if mode == "upi" or "card":
    print("Digital payment")
# Write it out instead:
if mode == "upi" or mode == "card":
    print("Digital payment")
else:
    print("Cash payment")
