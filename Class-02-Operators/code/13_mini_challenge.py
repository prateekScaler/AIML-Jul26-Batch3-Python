# Mini challenge: can they enter the event?
# Rule: at least 18 AND has an ID. Write your own version first.

age = int(input("Enter your age: "))
has_id = input("Do you have an ID? ")

can_enter = age >= 18 and has_id == "yes"

print("Can enter:", can_enter)

# Try typing Yes with a capital Y. Why does it print False?
