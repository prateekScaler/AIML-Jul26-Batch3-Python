# Nested in practice: a UPI login. (No real app keeps a PIN in the code.)
upi_id = input("Enter UPI ID: ")
pin = input("Enter UPI PIN: ")

if upi_id == "sumit@paisapay":
    if pin == "4321":
        print("Login successful")
    else:
        print("Incorrect PIN")
else:
    print("Unknown UPI ID")
