from audioop import add
import pymysql
import os
import database_func
from dotenv import load_dotenv

#Access Database

load_dotenv()
my_host = os.environ.get("mysql_host")
my_user = os.environ.get("mysql_user")
my_password = os.environ.get("mysql_pass")
my_database = os.environ.get("mysql_db")

 
def get_connection():   
    connection = pymysql.connect(
    host=my_host,
    user=my_user,
    password=my_password,
    database=my_database
    )
    return connection



# connection = get_connection()
# cursor = connection.cursor()
# cursor.execute("CREATE TABLE customers (customer_id INT AUTO_INCREMENT PRIMARY KEY, customer_name VARCHAR(2000), customer_phone INT)")
# connection.commit()
# cursor.close()
# connection.close()





# connection.commit()


# connection = get_connection()
# cursor = connection.cursor()
# cursor.execute("CREATE TABLE food_orders (order_ id INT PRIMARY KEY, product_id INT, quantity INT, price DECIMAL(10,0))")
# connection.commit()
# cursor.close()
# connection.close()

# connection = get_connection()
# cursor = connection.cursor()
# cursor.execute("CREATE TABLE orders (order_ id INT PRIMARY KEY, courier_id INT, order_total DECIMAL(10,0))")
# connection.commit()
# cursor.close()
# connection.close()



# connection = get_connection()
# cursor = connection.cursor()
# try:

#     entry = """INSERT INTO couriers (courier_id, courier_name, courier_phone, food_price, quantity) 
#                            VALUES (%s, %s, %s, %s, %s) """

#     insert = [(1, 'Chocolate McChoclate Cake', 'Cake that is chocolate what more do you need to know', 20, 100),
#                          (2, 'Salad', 'A boring choice for a boring person', 666.00, 100),
#                          (3, 'Hot Chocolate', 'With Coconut milk to bring that warm chocolately cozyness', 10, 100),
#                          (4, 'Costalot Special', 'Two slices of toast with jam but we will charge the cost of a whole loaf', 12, 100 ),
#                          (5, 'Vegan Pepperoni Pizza', 'With lots of meat and chesee from animals just what you Vegans want right', 23, 100)]

#     cursor = connection.cursor()

#     connection.commit()
#     print(cursor.rowcount, "Record inserted successfully into Laptop table")

# except pymysql.Error as error:
#     print("Failed to insert record into MySQL table {}".format(error))

# finally:
#     if connection.is_connected():
#         cursor.close()
#         connection.close()
#         print("MySQL connection is closed")



# def add_to_db (db_name ,db_headings, values):
#     try:
#         cursor.execute(f"""
#         INSERT INTO {db_name} ({db_headings})

#         VALUES ({values});

#         """)
#     except: 
#         print("Sorry that didnt work")
