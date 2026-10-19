# f-strings: values and expressions inside the braces. No str() needed.
name = "Rashi"
age = 20

print("My name is " + name + " and I am " + str(age) + " years old.")
print(f"My name is {name} and I am {age} years old.")

price = 99.5678
quantity = 3
print(f"Total: {price * quantity}")
print(f"Price: {price:.2f}")

amount = 600
fee = 5
print(f"Total ₹{amount + fee}")
print("Hello {name}")        # without the f, the braces are just text
