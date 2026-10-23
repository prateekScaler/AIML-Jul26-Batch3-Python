# A dictionary of lists: every score survives.
scores = {
    "Prasad": [90, 85, 95],
    "Madhumaya": [70, 75, 80]
}
print(scores["Prasad"])
print(scores["Prasad"][0])

# A dictionary of dictionaries: a lookup inside a lookup.
contacts = {
    "sumit@ybl": {"name": "Sumit", "city": "Bengaluru"},
    "parveen@okaxis": {"name": "Parveen", "city": "Pune"}
}
print(contacts["sumit@ybl"]["city"])

# A list of tuples: unpack each record in the for line.
payments = [("Sumit", 600, "upi"),
            ("Parveen", 250, "card"),
            ("Sumit", 1500, "upi")]
for name, amount, mode in payments:
    print(name, amount, mode)
