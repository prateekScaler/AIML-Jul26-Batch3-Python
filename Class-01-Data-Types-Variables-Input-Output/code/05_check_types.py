# type() answers: what kind of data is stored here?

age = 25
height = 5.8
name = "Kishor"
is_student = True

print(type(age))          # <class 'int'>
print(type(height))       # <class 'float'>
print(type(name))         # <class 'str'>
print(type(is_student))   # <class 'bool'>

# Quotes and the decimal point decide the type, not how the value looks:
print(type(42))       # <class 'int'>
print(type(42.0))     # <class 'float'>
print(type("42"))     # <class 'str'>
print(type("True"))   # <class 'str'>
