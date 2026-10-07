# score += 5 means exactly: score = score + 5

score = 10

score += 5
print(score)    # 15

score -= 2
print(score)    # 13

score *= 2
print(score)    # 26

# A classic slip: =+ is not +=
balance = 100
balance =+ 50   # this is plain assignment of +50
print(balance)  # 50
