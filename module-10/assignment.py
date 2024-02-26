from __future__ import print_function

import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'outland_adventures'

TABLES = {}


TABLES["departments"] = (
    """
    CREATE TABLE `departments` (
        `department_id` INT NOT NULL AUTO_INCREMENT,
        `department_name` varchar(255) NOT NULL,
        PRIMARY KEY (`department_id`))
        ENGINE=InnoDB
    """
)

TABLES['employees'] = (
    """
    CREATE TABLE `employees` (
        `employee_id` int NOT NULL AUTO_INCREMENT,
        `first_name` varchar(255) NOT NULL,
        `last_name` varchar(255) NOT NULL,
        `nick_name` varchar(255),
        `hire_date` date NOT NULL,
        `department_id` int NOT NULL,
        PRIMARY KEY (`employee_id`),
        CONSTRAINT `fk_employee_department` FOREIGN KEY (`department_id`) 
            REFERENCES `departments` (`department_id`) ON DELETE RESTRICT ON UPDATE CASCADE)
        ENGINE=InnoDB
    """
)

TABLES['customers'] = (
    """
    CREATE TABLE `customers` (
        `customer_id` INT NOT NULL AUTO_INCREMENT,
        `first_name` varchar(255) NOT NULL,
        `last_name` varchar(255) NOT NULL,
        `email` varchar(255) NOT NULL,
        PRIMARY KEY (`customer_id`))
        ENGINE=InnoDB
    """
)

TABLES['locations'] = (
    """
    CREATE TABLE `locations` (
        `location_id` INT NOT NULL AUTO_INCREMENT,
        `location_name` varchar(255) NOT NULL,
        `region` varchar(255) NOT NULL,
        `country` varchar(255) NOT NULL,
        `city` varchar(255) NOT NULL,
        PRIMARY KEY (`location_id`))
        ENGINE=InnoDB
    """
)

TABLES['trips'] = (
    """
    CREATE TABLE `trips` (
        `trip_id` INT NOT NULL AUTO_INCREMENT,
        `trip_name` varchar(255) NOT NULL,
        `trip_date` date NOT NULL,
        `trip_price` INT NOT NULL,
        `location_id` INT NOT NULL,
        PRIMARY KEY (`trip_id`),
        CONSTRAINT `fk_trip_location` FOREIGN KEY (`location_id`) 
            REFERENCES `locations` (`location_id`) ON DELETE RESTRICT ON UPDATE CASCADE)
        ENGINE=InnoDB
    """
)

TABLES['equipment'] = (
    """
    CREATE TABLE `equipment` (
        `equipment_id` INT NOT NULL AUTO_INCREMENT,
        `equipment_name` varchar(255) NOT NULL,
        `manufacturing_date` date NOT NULL,
        `manufacturer` varchar(255) NOT NULL,
        `model` varchar(255),
        PRIMARY KEY (`equipment_id`))
        ENGINE=InnoDB
    """
)

TABLES['inventory'] = (
    """
    CREATE TABLE `inventory` (
        `item_id` INT NOT NULL AUTO_INCREMENT,
        `item_name` varchar(255) NOT NULL,
        `original_price` INT NOT NULL,
        `rent_price` INT NOT NULL,
        `sale_price` INT NOT NULL,
        `purchase_date` date NOT NULL,
        `condition` varchar(255) NOT NULL,
        `location_id` INT,
        `equipment_id` INT NOT NULL,
        PRIMARY KEY (`item_id`),
        CONSTRAINT `fk_inventory_location` FOREIGN KEY (`location_id`)
            REFERENCES `locations` (`location_id`) ON DELETE RESTRICT ON UPDATE CASCADE,
        CONSTRAINT `fk_inventory_equipment` FOREIGN KEY (`equipment_id`)
            REFERENCES `equipment` (`equipment_id`) ON DELETE RESTRICT ON UPDATE CASCADE)
        ENGINE=InnoDB
    """
)



TABLES['orders'] = (
    """
    CREATE TABLE `orders` (
        `order_id` INT NOT NULL AUTO_INCREMENT,
        `order_type` enum('trip', 'equipment') NOT NULL,
        `order_date` date NOT NULL,
        `quantity` INT NOT NULL,
        `payment_method` varchar(255) NOT NULL,
        `payment_status` varchar(255) NOT NULL,
        `customer_id` INT NOT NULL,
        `item_id` INT,
        `trip_id` INT NOT NULL,
        `employee_id` INT NOT NULL,
        PRIMARY KEY (`order_id`),
        CONSTRAINT `fk_order_customer` FOREIGN KEY (`customer_id`)
            REFERENCES `customers` (`customer_id`) ON DELETE RESTRICT ON UPDATE CASCADE,
        CONSTRAINT `fk_order_inventory` FOREIGN KEY (`item_id`)
            REFERENCES `inventory` (`item_id`) ON DELETE RESTRICT ON UPDATE CASCADE,
        CONSTRAINT `fk_order_trip` FOREIGN KEY (`trip_id`)
            REFERENCES `trips` (`trip_id`) ON DELETE RESTRICT ON UPDATE CASCADE,
        CONSTRAINT `fk_order_employee` FOREIGN KEY (`employee_id`)
            REFERENCES `employees` (`employee_id`) ON DELETE RESTRICT ON UPDATE CASCADE)
        ENGINE=InnoDB
    """
)




add_department = (
    """
    INSERT INTO `departments`
    (`department_name`)
    VALUES (%s)
    """
)

DEPARTMENTS = [
    ('Owners',),
    ('Guides',),
    ('Marketing',),
    ('Supplies',),
    ('E-commerce',)
]

add_employee = (
    """
    INSERT INTO `employees`
    (first_name, last_name, nick_name, hire_date, department_id)
    VALUES (%s, %s, %s, %s, %s)
    """
)

EMPLOYEES = [
    ('Blythe', 'Timmerson', '', '2020-01-01', 1),
    ('Jim', 'Ford', '', '2020-01-01', 1),
    ('John', 'MacNell', 'Mac', '2020-03-02', 2),
    ('D.B.', 'Marland', 'Duke', '2020-03-08', 2),
    ('Anita', 'Gallegos', '', '2020-04-05', 3),
    ('Dimitrios', 'Stravopolous', '', '2020-05-15', 4),
    ('Mei', 'Wong', '', '2020-06-20', 5)
]

add_customers = (
    """
    INSERT INTO `customers`
    (first_name, last_name, email)
    VALUES (%s, %s, %s)
    """
)

CUSTOMERS = [
    ('John', 'Amigon', 'john.amigon@gmail.com'),
    ('Ivan', 'Pryymak', 'ivan.pryymak@gmail.com'),
    ('Mariana', 'Vyshnevska', 'mariana.vyshnevska@gmail.com'),
    ('Michael', 'Jackson', 'michael.jackson@gmail.com'),
    ('Bruce', 'Willis', 'bruce.willis@gmail.com'),
    ('Stan', 'Lee', 'stan.lee@gmail.com')
]

add_equipment = (
    """
    INSERT INTO `equipment`
    (equipment_name, manufacturing_date, manufacturer, model)
    VALUES (%s, %s, %s, %s)
    """
)

EQUIPMENT = [
    ('Backpack', '2023-01-15', 'Travel-co', 'BCKPCK-5145'),
    ('Snow boots', '2023-02-06', 'Snow-co', 'Boots-1124'),
    ('Tent', '2020-11-24', 'Travel-co', 'Tent-8869'),
    ('Travel pillow', '2022-10-11', 'Comfy-co', 'Pillow-8874'),
    ('Power bank', '2021-08-07', 'Electronics-co', 'Bank-4412'),
    ('Money belt', '2017-05-16', 'Wear-co', 'Belt-2214'),
]

add_location = (
    """
    INSERT INTO `locations`
    (location_name, region, country, city)
    VALUES (%s, %s, %s, %s)
    """
)

LOCATIONS = [
    ('Shewa', 'Africa', 'Ethiopia', 'Addis Ababa'),
    ('Chongqing', 'Asia ', 'China', 'Beijing'),
    ('Eastern Spain', 'Southern Europe', 'Spain', 'Barcelona'),
    ('Cape Town', 'Africa', 'South Africa', 'Cape Town'),
    ('Pyramids', 'Africa', 'Egypt', 'Cairo'), 
    ('Islands', 'Asia', 'Indonesia', 'Bali')

  
]

add_inventory = (
    """
    INSERT INTO `inventory`
    (`item_name`, `original_price`, `rent_price`, `sale_price`, `purchase_date`, `condition`, `location_id`, `equipment_id`)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
)

INVENTORY = [
    ('Backpack', 40, 20, 80, '2023-02-10', 'Like new', 1, 1),
    ('Snow boots', 80, 40, 150, '2023-02-25', 'Like new', 2, 2),
    ('Tent', 200, 100, 400, '2021-01-10', 'Satisfactory', 5, 3),
    ('Travel pillow', 20, 10, 35, '2023-02-16', 'Like new', 3, 4),
    ('Power bank', 30, 15, 50, '2021-10-10', 'Satisfactory', 4, 5),
    ('Money belt', 10, 5, 20, '2018-01-19', 'Worn out', 6, 6)
]

add_trip = (
    """
    INSERT INTO trips
    (trip_name, trip_date, trip_price, location_id)
    VALUES (%s, %s, %s, %s)
    """
)

TRIPS = [
    ('Suba Menagesha', '2024-05-25', 4500, 1),
    ('Didessa', '2024-06-14', 3500, 1),
    ('Nanshan', '2024-08-07', 4000, 2),
    ('Tieshanping', '2024-09-08', 4250, 2),
    ('Serra de Collserola', '2024-10-08', 5000, 3),
    ('Zwolf Apostel', '2024-11-08', 3900, 4),
    ('Ancient Egypt', '2025-03-14', 4500, 5),
    ('Air Terjun Juwuk Manis', '2025-04-14', 4170, 6)


]

add_order = (
    """
    INSERT INTO `orders`
    (order_type, order_date, quantity, payment_method, payment_status, customer_id, item_id, trip_id, employee_id)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
)

ORDERS = [
    ('trip', '2024-01-01', 1, 'Credit card', 'Completed', 1, None, 1, 3),
    ('trip', '2023-11-15', 1, 'Bank Transfer', 'Completed', 2, None, 2, 4),
    ('trip', '2023-10-01', 2, 'Credit Card', 'Completed', 3, None, 3, 4),
    ('equipment', '2024-01-01', 1, 'Credit card', 'Completed', 1, 1, 1, 3),
    ('equipment', '2023-11-15', 1, 'Bank Transfer', 'Completed', 2, 2, 2, 4),
    ('equipment', '2023-10-01', 1, 'Credit card', 'Completed', 3, 3, 3, 4),
    ('trip', '2022-11-11', 2, 'Cash', 'Completed', 4, None, 4, 3),
    ('trip', '2021-10-01', 2, 'Cash', 'Completed', 5, None, 5, 3),
    ('trip', '2024-02-02', 2, 'Cash', 'Completed', 6, None, 6, 4)
]


cnx = mysql.connector.connect(user='adventures_user', password = 'adventures')
cursor = cnx.cursor()

cursor.execute("DROP DATABASE IF EXISTS outland_adventures")


def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    cursor.execute("USE {}".format(DB_NAME))
    

except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        print("Database {} created successfully.".format(DB_NAME))
        cnx.database = DB_NAME
    else:
        print(err)
        exit(1)



for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")


for department in DEPARTMENTS:
    cursor.execute(add_department, department)

for employee in EMPLOYEES:
    cursor.execute(add_employee, employee)

for customer in CUSTOMERS:
    cursor.execute(add_customers, customer)

for equipment in EQUIPMENT:
    cursor.execute(add_equipment, equipment)

for location in LOCATIONS:
    cursor.execute(add_location, location)

for item in INVENTORY:
    cursor.execute(add_inventory, item)

for trip in TRIPS:
    cursor.execute(add_trip, trip)

for order in ORDERS:
    cursor.execute(add_order, order)

cnx.commit()

cursor.close()
cnx.close()


