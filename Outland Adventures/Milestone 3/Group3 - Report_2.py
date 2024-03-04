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

query = ('''SELECT YEAR(order_date) as Year, COUNT(*) as Bookings FROM orders o
		  inner join trips t
		  on o.trip_id = t.trip_id
         inner join locations l
         on t.location_id = l.location_id
            WHERE l.region= 'Southern Europe' AND order_type = 'Trip' 
            Group By YEAR(order_date)
            Order By YEAR(order_date)  ''')

cursor.execute(query)
southern_europe_count = cursor.fetchall()


# Get column names
column_names = [desc[0] for desc in cursor.description]


print("Report 2: Booking Trends")
print("----------------------------")

print("Trips booked in Southern Europe:")
print(tabulate(southern_europe_count, headers=column_names, tablefmt='grid'))

query = ('''SELECT YEAR(order_date) as Year, COUNT(*) as Bookings FROM orders o
		  inner join trips t
		  on o.trip_id = t.trip_id
         inner join locations l
         on t.location_id = l.location_id
            WHERE l.region= 'Africa' AND order_type = 'Trip' 
            Group By YEAR(order_date)
            Order By YEAR(order_date)  ''')

cursor.execute(query)
africa_count = cursor.fetchall()


# Get column names
column_names = [desc[0] for desc in cursor.description]

print("Trips booked in Africa:")
print(tabulate(africa_count, headers=column_names, tablefmt='grid'))


query = ('''SELECT YEAR(order_date) as Year, COUNT(*) as Bookings  FROM orders o
		  inner join trips t
		  on o.trip_id = t.trip_id
         inner join locations l
         on t.location_id = l.location_id
            WHERE l.region= 'Asia' AND order_type = 'Trip' 
            Group By YEAR(order_date)
            Order By YEAR(order_date)  ''')

cursor.execute(query)
asia_count = cursor.fetchall()


# Get column names
column_names = [desc[0] for desc in cursor.description]

print("Trips booked in Asia:")
print(tabulate(asia_count, headers=column_names, tablefmt='grid'))




# Close the connection
conn.close()