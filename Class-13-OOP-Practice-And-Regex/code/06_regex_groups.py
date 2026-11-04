# Capturing groups: brackets in the pattern pull out the pieces you want.
import re

text = "Name: Rex, Age: 3"
match = re.search(r"Name: (\w+), Age: (\d+)", text)
print(match.group(0))     # the whole match
print(match.group(1))     # Rex
print(match.group(2))     # 3

# findall with groups returns tuples of the groups, not whole matches
text = "Name: Rex, Age: 3; Name: Fido, Age: 5"
print(re.findall(r"Name: (\w+), Age: (\d+)", text))

# a bank SMS: amount, account tail, payee
sms = "Rs.600 debited from a/c XX4321 to SUMIT on 04-11-26 via UPI"
m = re.search(r"Rs\.(\d+) debited from a/c XX(\d{4}) to (\w+)", sms)
amount, tail, payee = m.groups()
print(amount, tail, payee)

# log lines: timestamp, level, message
logs = [
    "2026-11-04 21:05:02 ERROR Failed to connect to database",
    "2026-11-04 21:05:05 INFO Retry succeeded",
    "2026-11-04 21:06:40 WARNING Disk usage above 90%",
]
pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)"
for line in logs:
    timestamp, level, message = re.match(pattern, line).groups()
    print(f"[{level}] {timestamp} - {message}")
