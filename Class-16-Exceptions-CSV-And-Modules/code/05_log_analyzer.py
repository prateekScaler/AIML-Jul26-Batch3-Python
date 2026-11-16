# Mini project: read visits from a CSV, count the errors, write a summary.
import csv

with open("visits.csv", "w", newline="") as f:
    f.write("page,status_code\n/home,200\n/login,200\n/admin,403\n/checkout,500\n")

def analyze_visits(filename):
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            rows = list(reader)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return

    total = len(rows)
    errors = [r for r in rows if int(r["status_code"]) >= 400]

    print(f"Total requests: {total}")
    print(f"Errors: {len(errors)}")

    with open("summary.txt", "w") as file:
        file.write(f"Total requests: {total}\n")
        file.write(f"Errors: {len(errors)}\n")

analyze_visits("visits.csv")
analyze_visits("nothing_here.csv")

with open("summary.txt") as f:
    print(f.read())
