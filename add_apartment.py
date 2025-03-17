import sys
from db import Db
db = Db()

args = sys.argv[1:]

if len(args) < 2:
    print("Please provide location and apartment name\n"
          "Example: python add_apartment.py 'location(City Name)' 'Apartment Name' 'X - if apartment is premium'")
    sys.exit(1)

if len(args[0]) > 33 or len(args[1]) > 33:
    print("Location and/or City Name cannot be more than 32 characters")
    sys.exit(1)

location = args[0].lower()
apartment_name = args[1].lower()
premium_status = 1 if len(args) > 2 else None

sql_values = (location, apartment_name, premium_status)
query = "INSERT INTO apartment_table (location, apartment_name, premium_status) VALUES (%s, %s, %s)"

db.execute(query, sql_values)
