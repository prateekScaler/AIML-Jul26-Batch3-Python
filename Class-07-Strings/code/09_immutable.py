# Strings cannot be changed in place. Every string method gives back a new string: catch it.
word = "Python"
# word[0] = "J"               # TypeError: 'str' object does not support item assignment
word = "J" + word[1:]
print(word)

text = "hello"
text.upper()                   # a new string, thrown away
print(text)

text = text.upper()            # caught
print(text)
