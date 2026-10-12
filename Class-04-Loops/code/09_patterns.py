# Four loop patterns: accumulate, count, find, filter.
# Same skeleton every time: loop, check, update. Start the variable above the loop.
total = 0
for i in range(1, 6):
    total += i
print("Total 1 to 5:", total)

amounts = [250, 1200, 80, 5000, 999, 1500]

# count the big ones
count = 0
for amount in amounts:
    if amount >= 1000:
        count += 1
print("Big payments:", count)

# find: is there a payment of exactly 5000?
found = False
for amount in amounts:
    if amount == 5000:
        found = True
        break
print("Found 5000:", found)

# filter: print only the big ones
for amount in amounts:
    if amount < 1000:
        continue
    print(amount)
