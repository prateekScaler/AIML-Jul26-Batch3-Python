# in / not in ask: is this inside that?

upi_id = "rajani@paisapay"
print("@" in upi_id)        # True
print(" " not in upi_id)    # True

# == asks: same value?   is asks: the very same object?
a = [100, 200]
b = [100, 200]
print(a == b)   # True
print(a is b)   # False: two separate lists that happen to hold the same values

# Where is says True: two names for one object
b = a
print(a is b)   # True
b += [300]
print(a)        # [100, 200, 300]  the same list, seen through either name
# The everyday use of is: checking for "nothing", x is None (functions class).
