# Q4. Password strength validator (Classes 5 and 7)
def validate_password(password, min_length=8, require_special=True):
    issues = []
    if len(password) < min_length:
        issues.append("too short")
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    for ch in password:
        if ch.isupper():
            has_upper = True
        if ch.islower():
            has_lower = True
        if ch.isdigit():
            has_digit = True
        if ch in "!@#$%^&*":
            has_special = True
    if not has_upper:
        issues.append("no uppercase")
    if not has_lower:
        issues.append("no lowercase")
    if not has_digit:
        issues.append("no digit")
    if require_special and not has_special:
        issues.append("no special character")
    if " " in password:
        issues.append("has a space")
    return len(issues) == 0, issues          # two values: a tuple

def report(passwords):
    for password in passwords:
        is_strong, issues = validate_password(password)
        if is_strong:
            print(f"{password} -> STRONG")
        else:
            print(f"{password} -> WEAK: {', '.join(issues)}")

print(validate_password("Pass1234!"))                        # positional
print(validate_password("abc", min_length=4, require_special=False))   # keyword
print(validate_password("Short1!"))                          # defaults

report(["Pass1234!", "abc", "no spaces here 1A!"])

# sorted with a lambda key: longest first (a preview of Class 9)
by_length = sorted(["Pass1234!", "abc", "no spaces here 1A!"], key=lambda p: len(p), reverse=True)
print(by_length)

# Reading a global inside a function works. Assigning to it without the
# global keyword makes a new local variable instead, and the global is unchanged.
