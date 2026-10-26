# Q5. Text cleaner and analyzer (Classes 6 and 7)
text = "  Python is simple. python is POWERFUL! Learning Python for AI is fun, and AI needs Python.  "

clean = text.strip().lower()                       # 1. outer spaces off, one case
clean = clean.replace(".", "").replace(",", "").replace("!", "")   # 2. no punctuation
words = clean.split()                              # 3. a list of words
print(words)

long_words = [w for w in words if len(w) > 3]     # 4. keep the long ones
print(long_words)

lengths = [len(w) for w in words]                  # 5. one number per word
print(lengths)

longest = words[0]                                 # 6. longest and shortest
shortest = words[0]
for w in words:
    if len(w) > len(longest):
        longest = w
    if len(w) < len(shortest):
        shortest = w
print(longest, shortest)

unique = []                                        # 7. unique, in first-seen order
for w in words:
    if w not in unique:
        unique.append(w)
print(unique)

print(clean.title())                               # 8. title case

def is_palindrome(word):                           # 9. first and last word
    return word == word[::-1]

print(is_palindrome(words[0]), is_palindrome(words[-1]))

print(" ".join(words[::-1]))                       # 10. reversed word by word
