# break leaves the loop. continue skips one pass. pass does nothing.
print("break:")
for txn in range(1, 11):
    if txn == 6:
        break
    print("Transaction", txn, "done")

print("continue:")
for txn in range(1, 6):
    if txn == 3:
        continue
    print("Transaction", txn, "done")

print("pass:")
for i in range(5):
    if i == 3:
        pass
    else:
        print(i)
