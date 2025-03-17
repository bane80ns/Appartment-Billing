import sys
from db import Db
from datetime import datetime

db = Db()
current_date = datetime.now().date()
args = sys.argv[1:]


if len(args) != 1:
    print('"Please provide correct data:\n'
          'Example:\n'
          'python pay_expense.py "paid" or  python pay_expense.py "unpaid"')
    sys.exit(1)


if args[0] == 'paid':
    status_variable = "paid"


elif args[0] == 'unpaid':
    status_variable = "unpaid"


else:
    print('"Please provide correct data:\n'
          'Example:\n'
          'python pay_expense.py "paid" or  python pay_expense.py "unpaid"')
    sys.exit(1)



paid_query = """
    SELECT 
        a.location, 
        CASE 
            WHEN a.premium_status = 1 THEN CONCAT(a.apartment_name, ' X') 
            ELSE a.apartment_name 
        END AS apartment_name,
        e.paid_status
    FROM expenses_table e
    JOIN apartment_table a ON e.apartment_id = a.unique_id
    WHERE e.paid_status = %s;
"""


results = db.query(paid_query, (status_variable,))


for row in results:
    print(row)  # Prints each row of the result