# A key points to one value. Assign again and the old value is gone.
scores = {}
scores["Aanand"] = 90
scores["Saurabh"] = 85
scores["Aanand"] = 95

print(scores)
print(len(scores))

# To keep every score, store a list under the key.
scores = {}
scores["Aanand"] = [90]
scores["Saurabh"] = [85]
scores["Aanand"].append(95)
print(scores)
