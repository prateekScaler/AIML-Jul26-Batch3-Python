# Mini project: count every word, then count the unique words.
sentence = "the cat sat on the mat the cat ran"
words = sentence.split()
print(words)

counts = {}
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)

unique_words = set(words)
print("Unique words:", len(unique_words))
