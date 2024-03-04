import mysql.connector
from tabulate import tabulate

# Connect to the MySQL database
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="adventures_user",
    password="adventures",
    database="outland_adventures",


)

cursor = conn.cursor()


# Query to count customers who bought equipment outright
cursor.execute('''SELECT COUNT(*) FROM Orders WHERE order_type = 'Buy' ''')
buy_count = cursor.fetchone()[0]

# Query to count customers who rented equipment
cursor.execute('''SELECT COUNT(*) FROM Orders WHERE order_type = 'Rent' ''')
rent_count = cursor.fetchone()[0]

# Display the report
print("Report 3: Equipment Sales")
print("----------------------------")
print("Customers who bought equipment outright:", buy_count)
print("Customers who rented equipment:", rent_count)

# Close the connection
conn.close()

