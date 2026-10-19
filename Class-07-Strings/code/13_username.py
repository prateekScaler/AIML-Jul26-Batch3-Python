# Mini challenge: a classroom username check with len, in and lower.
username = input("Enter username: ").strip()

starts_with_letter = username[0].lower() in "abcdefghijklmnopqrstuvwxyz"

if len(username) >= 5 and " " not in username and starts_with_letter:
    print("Username looks valid.")
else:
    print("Invalid username.")
