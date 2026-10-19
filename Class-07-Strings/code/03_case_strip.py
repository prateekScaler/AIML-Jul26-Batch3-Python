# lower, upper, title, strip: each gives back a new string. Chain them.
text = "Hello Python"
print(text.lower())
print(text.upper())

name = "   rashi sharma   "
print(name.title())
print(name.strip())
print(name.strip().title())

mode = "Card"
print(mode.lower() == "card", mode == "card")
