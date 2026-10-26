# Quick-fire: predict each line before you run it. Answers in the comments.
print(type(3/2), type(3//2), 2**3**2)      # <class 'float'> <class 'int'> 512

x = "5"
print(x*3, int(x)*3)                        # 555 15

print(bool(""), bool("0"), bool([]), bool([0]))   # False True False True

a = [1, 2, 3]
b = a
b.append(4)
print(a)                                    # [1, 2, 3, 4]: b and a are the same list

t = (1, 2, [3, 4])
t[2].append(5)
print(t)                                    # (1, 2, [3, 4, 5]): the list inside can change

print({1, 2, 3} & {2, 3, 4}, {1, 2, 3} - {2, 3, 4})   # {2, 3} {1}

s = "python"
print(s[::-2], s[1:4])                      # nhy yth

d = {"a": 1}
print(d.get("b", 0), d.get("b"), d)         # 0 None {'a': 1}: get never adds a key

