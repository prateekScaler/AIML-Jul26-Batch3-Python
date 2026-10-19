# Walk through a string one character at a time. Count the vowels.
word = "Python"
for character in word:
    print(character)

word = "education"
count = 0
for character in word:
    if character in "aeiou":
        count += 1
print("Vowels:", count)
