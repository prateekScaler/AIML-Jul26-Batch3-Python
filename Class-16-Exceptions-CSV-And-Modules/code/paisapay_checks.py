# Module file: paisapay_checks.py
# PaisaPay's checks, moved into their own module. paisapay_v16.py imports them.
import re


def clean(text):
    return text.strip().lower()


def is_valid_upi_id(upi_id):
    # letters, digits or dots, then @, then a bank handle of letters only
    return re.fullmatch(r"[a-z0-9.]+@[a-z]+", upi_id) is not None


def is_valid_pan(pan):
    # five letters, four digits, one letter: ABCDE1234F
    return re.fullmatch(r"[A-Z]{5}\d{4}[A-Z]", pan) is not None


def read_bank_sms(sms):
    # "Rs.600 debited from a/c XX4321 to SUMIT on 04-11-26 via UPI"
    m = re.search(r"Rs\.(\d+) debited from a/c XX(\d{4}) to (\w+)", sms)
    if m is None:
        return None
    amount, tail, payee = m.groups()
    return int(amount), tail, payee.title()


def mode_name(mode):
    match mode:
        case "upi":
            return "UPI"
        case "card":
            return "Card"
        case "netbanking":
            return "Net banking"
        case _:
            return "Unknown mode"
