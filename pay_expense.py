import sys
from db import Db
from datetime import datetime
db = Db()

current_date = datetime.now().date()


args = sys.argv[1:]

if len(args) != 1:
    print('"Please provide correct data:\n'
          'Example:\n'
          'python pay_expense.py "1"')
    sys.exit(1)

bill_id = int(args[0])
print(bill_id)
paid_status = "paid"

query = "UPDATE expenses_table SET paid_status = %s, payment_date = %s WHERE id = %s"
sql_values = (paid_status, current_date, bill_id)
db.execute(query, sql_values)