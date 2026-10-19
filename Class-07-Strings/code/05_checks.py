# startswith, endswith and in give back a bool. They belong inside an if.
filename = "report.pdf"
upi_id = "rashi@okaxis"

print(filename.startswith("report"))
print(filename.endswith(".pdf"))
print("@" in upi_id)
print(" " in upi_id)

sms = "Rs 600 debited from A/c XX4444 via UPI"
print(sms.startswith("Rs"), "UPI" in sms, sms.endswith("upi"))
