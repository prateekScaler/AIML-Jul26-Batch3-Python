# match / case: one variable against exact values. Python 3.10 or newer.
mode = input("Payment mode: ")

match mode:
    case "upi":
        print("Opening UPI app...")
    case "card":
        print("Enter card PIN")
    case "netbanking":
        print("Redirecting to your bank")
    case _:
        print("Unknown mode")     # the wildcard: anything left over

# Try "upi", then "UPI": a case is an exact, case-sensitive match.
