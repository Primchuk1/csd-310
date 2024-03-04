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

# Query to retrieve inventory items that are over five years old
cursor.execute(
    '''select item_id "Item ID",i.item_name "Item Name", Manufacturer , Model , 
              TIMESTAMPDIFF(YEAR,manufacturing_date,CURDATE()) "Equipment Ages"
              from equipment e
              inner join inventory i
              on e.equipment_ID = i.equipment_ID
             where TIMESTAMPDIFF(YEAR,manufacturing_date,CURDATE()) > 5 ;''')
aged_items = cursor.fetchall()

# Get column names
column_names = [desc[0] for desc in cursor.description]

# Display the report
print("Report 1: Aged Inventory Items")
print("The table below displays a list of all equipment items that are more than five years old..")
#print(", ".join(column_names))  # Print column headers

print(tabulate(aged_items, headers=column_names, tablefmt='grid'))

#for item in aged_items:
 #   print(item)

# Close the connection
conn.close()