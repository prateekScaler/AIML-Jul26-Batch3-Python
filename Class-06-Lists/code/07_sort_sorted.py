# sort() rearranges the list in place and gives back None.
# sorted() gives back a new sorted list and leaves the original untouched.
numbers = [50, 10, 40, 20, 30]
numbers.sort()
print(numbers)

names = ["Vinay", "Akash", "Shubhodip", "Hitender"]
names.sort()
print(names)

numbers.sort(reverse=True)
print(numbers)

numbers = [50, 10, 40, 20, 30]
sorted_numbers = numbers.sort()
print(sorted_numbers)        # None: sort() hands nothing back
print(numbers)               # but the list is sorted

numbers = [50, 10, 40, 20, 30]
new_list = sorted(numbers)
print(new_list)
print(numbers)
