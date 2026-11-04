# Regular expressions: describe the shape of text, not the exact text.
# search finds a pattern anywhere; match only at the start; fullmatch needs the whole string.
import re

text = "concatenate"
print(re.search(r"cat", text))      # <re.Match object; span=(3, 6), match='cat'>
print(re.match(r"cat", text))       # None: the string starts with "con", not "cat"

# . is one blank to fill: exactly one character, any character
for word in ["cat", "cot", "ct", "coat"]:
    print(word, bool(re.search(r"c.t", word)))

# ^ is the starting line, $ is the finish line
messages = ["UPI paid", "Paid by UPI"]
for m in messages:
    print(m, bool(re.search(r"^UPI", m)))
for m in messages:
    print(m, bool(re.search(r"UPI$", m)))

# \ takes away the special job: \. is a real dot
name = "bill-pdf"
print(bool(re.search(r"bill.pdf", name)))   # True: the dot fills the blank
print(bool(re.search(r"bill\.pdf", name)))  # False: needs a real dot

# | means or
for w in ["by UPI", "by card", "by cash"]:
    print(w, bool(re.search(r"UPI|card", w)))

# [ ] picks one from the menu
for w in ["cat", "bat", "rat"]:
    print(w, bool(re.search(r"[cb]at", w)))

# ranges: one lowercase letter, one capital, one digit
for w in ["upi", "UPI", "123"]:
    print(w, bool(re.search(r"[a-z]", w)), bool(re.search(r"[A-Z]", w)), bool(re.search(r"[0-9]", w)))

# ^ inside the brackets means not
for w in ["123", "12a"]:
    print(w, bool(re.search(r"[^0-9]", w)))

# short forms: \d a digit, \w a word character, \s whitespace
print(bool(re.search(r"\d", "Room 42")))         # True
for w in ["a", "1", "_", "-"]:
    print(w, bool(re.search(r"\w", w)))
print(bool(re.search(r"\s", "UPI paid")))        # True

# a capital flips the meaning: \D \W \S
print(bool(re.search(r"\D", "123")))             # False
print(bool(re.search(r"\W", "a_1")))             # False
print(bool(re.search(r"\S", "   ")))             # False

# all of it together
print(bool(re.search(r"[aeiou]", "sky")))        # False: no vowel
print(bool(re.search(r"^\w+$", "hello world")))  # False: \w has no space

# + one or more, * zero or more, ? zero or one, of the thing before
for w in ["gd", "god", "good"]:
    print(w, bool(re.search(r"go+d", w)), bool(re.search(r"go*d", w)))
for w in ["color", "colour", "colouur"]:
    print(w, bool(re.search(r"colou?r", w)))

# { } gives the exact count: {5} means exactly five
for number in ["98765-43210", "9876-43210", "98765-432100", "9876543210"]:
    print(number, bool(re.fullmatch(r"\d{5}-\d{5}", number)))

# where these help in real work
print(re.sub(r"[^0-9]", "", "1,25,000"))         # 125000: clean an amount
print(re.findall(r"\d{6}", "Your OTP is 482913"))  # ['482913']: read an OTP
print(re.sub(r"\s+", " ", "UPI    paid   now"))   # UPI paid now: tidy pasted text
print(re.findall(r"\S+@\S+", "Pay sumit@ybl today"))  # ['sumit@ybl']: pull out an ID
print(bool(re.search(r"pdf$", "bill.pdf.exe")))  # False: catch a disguised file

# findall: every match, as a list
sms = "Rs.600 sent to sumit@ybl, Rs.250 to vamsi@oksbi, Rs.1500 to sathvik@paytm"
print(re.findall(r"\d+", sms))
print(re.findall(r"\w+@\w+", sms))
