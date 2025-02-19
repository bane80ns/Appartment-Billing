import sys
from db import Db
from datetime import datetime
import re
db = Db()

date_pattern = r"\d{2}/\d{2}/\d{4}"

args = sys.argv[1:]
if len(args) != 4:
    print("Must be 4 arguments\n"
          "Example:\n"
          "python booking.py 'id' 'booking_start_date' 'booking_end_date' 'client_jmbg'\n"
          "python booking.py '23' '05/05/2025' '06/05/2025' '2205979300022'")
    sys.exit(1)

if args[0].isdigit():
    apartment_id = int(args[0])
else:
    print("id must be an integer")
    sys.exit(1)

if re.fullmatch(date_pattern, args[1]):
    booking_start_date_string = args[1]
    booking_start_date_object = datetime.strptime(booking_start_date_string, "%d/%m/%Y")
    booking_start_date_formatted = booking_start_date_object.strftime("%Y-%m-%d")
else:
    print("Date must be in the format dd/mm/yyyy")
    sys.exit(1)


if re.fullmatch(date_pattern, args[2]):
    booking_end_date_string = args[2]
    booking_end_date_object = datetime.strptime(booking_end_date_string, "%d/%m/%Y")
    booking_end_date_formatted = booking_end_date_object.strftime("%Y-%m-%d")
else:
    print("Date must be in the format dd/mm/yyyy")
    sys.exit(1)


if re.fullmatch(r"\d{13}", args[3]):
    client_jmbg = int(args[3])
else:
    print("Client JMBG is not valid / Must have 13 digits")
    sys.exit(1)

sql_values = (apartment_id, booking_start_date_formatted, booking_end_date_formatted, client_jmbg)
query = "INSERT INTO rent_table (apartment_id, booking_start_date, booking_end_date, client_jmbg) VALUES (%s, %s, %s, %s)"

db.execute(query, sql_values)
