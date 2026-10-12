# Mini challenge: keep asking until the lucky number is guessed.
# number = 0 gives the condition a safe starting value that is not 7.
number = 0

while number != 7:
    number = int(input("Guess the number: "))

    if number < 7:
        print("Too low!")
    elif number > 7:
        print("Too high!")

print("Correct! You won ₹7 cashback")
