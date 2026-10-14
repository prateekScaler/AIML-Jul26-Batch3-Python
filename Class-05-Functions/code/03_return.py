# print shows a value to the human. return hands it back to the program.
# A function with no return hands back None.
def add_print(a, b):
    print(a + b)

result = add_print(10, 20)
print("stored:", result)          # None: nothing was returned

def add(a, b):
    return a + b

result = add(10, 20)
print("stored:", result)          # 30

def square(number):
    return number * number

print(square(5) + 10)             # a returned value can be used anywhere

def test():
    print("Start")
    return 10
    print("End")                  # never runs: return ends the function

test()
