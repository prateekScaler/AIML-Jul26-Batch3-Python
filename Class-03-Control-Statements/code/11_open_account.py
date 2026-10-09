# Mini project: open a PaisaPay account.
# Rule: at least 18 years old AND KYC completed.
age = int(input("Enter your age: "))
kyc_done = input("KYC completed? (yes/no): ")

if age >= 18 and kyc_done == "yes":
    print("Account opened. Welcome to PaisaPay!")
else:
    print("Sorry, you are not eligible.")

# Try 20/yes, 20/no, 16/yes, and 25/Yes (capital Y: text must match exactly).
