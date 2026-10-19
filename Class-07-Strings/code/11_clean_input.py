# Clean user input step by step, then greet with an f-string.
name = input("Enter your name: ")
name = name.strip()
name = name.title()
print(f"Hello, {name}!")
