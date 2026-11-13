# Why files: PaisaPay has many users, each with a name, a balance and a PIN.
# A dictionary lives in memory, and memory is cleared when the program ends.
# Run this twice. Nothing a user changed in the first run is still there.
accounts = {
    "rajani@okaxis": {"name": "Rajani", "balance": 1000, "pin": "4321"},
    "sumit@ybl": {"name": "Sumit", "balance": 2500, "pin": "1234"},
}
accounts["rajani@okaxis"]["balance"] -= 600     # Rajani pays ₹600
print(len(accounts), "accounts")
print("Rajani's balance:", accounts["rajani@okaxis"]["balance"])
