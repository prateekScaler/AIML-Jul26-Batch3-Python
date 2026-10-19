# Two practices: a name formatter and a sentence analyzer.
name = input("Enter your name: ").strip().title()
print(f"Hello, {name}!")

sentence = "Python is easy to learn"
print(len(sentence))
print(sentence[0])
print(sentence[-1])
print(sentence.upper())
print(sentence.replace("easy", "powerful"))
print(sentence.split())
