# replace changes every match. find gives the start index, or -1 when not found.
message = "I like Java"
message = message.replace("Java", "Python")
print(message)

text = "I love Python"
print(text.find("Python"))
print(text.find("Java"))

print("banana".replace("a", "o"))
