# Mini practice: ask for a name, an age and a favorite subject, then display them.
# Write your own version before reading this one.

name = input("What is your name? ")
age = int(input("How old are you? "))
subject = input("What is your favorite subject? ")

print("Hello,", name)
print("You are", age, "years old.")
print("Your favorite subject is", subject)

# Another correct way to write the first line (an f-string, covered later):
# print(f"Hello, {name}!")
