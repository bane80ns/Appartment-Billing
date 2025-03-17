import sys
from db import Db
import re
from datetime import datetime


db = Db()
date_pattern = r"\d{2}/\d{2}/\d{4}"

args = sys.argv[1:]
if len(args) != 5:
    print('"Please provide correct info:\n'
          'Example:\n'
          'python add_expense.py "1" "Struja" "500.27" "2025/02" "20/02/2025"')
    sys.exit(1)


if len(args[0]) > 33 or len(args[1]) > 33:
    print("Location and/or City Name cannot be more than 32 characters")
    sys.exit(1)


if args[0].isdigit():
    apartment_id = int(args[0])
else:
    expense_id = None
    print(f"apartment_id must be an integer")
    sys.exit(1)


bill_type = args[1].lower()


bill_amount_string = args[2]
try:
    bill_amount = float(bill_amount_string)
except ValueError:
    print("Error: bill_amount must be a valid float (12.50 or 100.0 or 100)!")
    sys.exit(1)


date_pattern_billing_period = r"\d{4}/\d{2}"
if re.fullmatch(date_pattern_billing_period, args[3]):
    billing_period_string = args[3]
    billing_period_formatted = billing_period_string.replace("/", "-") + "-01"
else:
    print("Billing Period date must be in format yyyy/mm")
    sys.exit(1)


date_pattern_due_date = r"\d{2}/\d{2}/\d{4}"
if re.fullmatch(date_pattern_due_date, args[4]):
    due_date_string = args[4]
    due_date_object = datetime.strptime(due_date_string, "%d/%m/%Y")
    due_date_string_formatted = due_date_object.strftime("%Y-%m-%d")
else:
    print("Due date must be in format dd/mm/yyyy")
    sys.exit(1)


billing_period = args[3]
due_date = args[4]

paid_status = "unpaid"

print(type(bill_amount))
print(bill_amount)
print(billing_period_formatted)
print(due_date_string_formatted)

sql_values = (apartment_id, bill_type, bill_amount, billing_period_formatted, due_date_string_formatted, paid_status)
query = "INSERT INTO expenses_table (apartment_id, bill_type, bill_amount, billing_period, due_date, paid_status) VALUES (%s, %s, %s, %s, %s, %s)"

db.execute(query, sql_values)