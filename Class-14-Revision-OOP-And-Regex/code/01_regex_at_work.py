# Regex at work: last class's tools on real Indian data.
# fullmatch for a whole field, search for one piece, findall for every piece.
import re

# a form field must be exactly six digits: fullmatch, not search
for pin in ["560001", "5600011", "56001"]:
    print(pin, re.fullmatch(r"\d{6}", pin) is not None, re.search(r"\d{6}", pin) is not None)

# one piece out of a message
sms = "Your OTP is 482913. Do not share it."
print(re.search(r"\d{6}", sms).group())

# every piece: findall gives strings, so convert before adding
text = "Rs.600 to Sumit, Rs.1500 to Vamsi"
amounts = re.findall(r"Rs\.(\d+)", text)
print(amounts)
print(sum(int(a) for a in amounts))

# a PAN typed in lowercase fails until it is cleaned
pan = "abcde1234f"
print(re.fullmatch(r"[A-Z]{5}\d{4}[A-Z]", pan) is not None)
print(re.fullmatch(r"[A-Z]{5}\d{4}[A-Z]", pan.upper()) is not None)
