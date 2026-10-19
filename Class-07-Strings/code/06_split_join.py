# split cuts a string into a list. join glues a list into a string.
sentence = "Python is easy"
words = sentence.split()
print(words)

data = "apple,banana,mango"
print(data.split(","))

print(" ".join(["Python", "is", "fun"]))
print(", ".join(["Apple", "Banana", "Mango"]))

upi_id = "rashi@okaxis"
parts = upi_id.split("@")
print(len(parts), parts[1])
