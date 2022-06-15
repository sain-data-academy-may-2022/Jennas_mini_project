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

connection = get_connection()
cursor = connection.cursor()

food_headers = ['food_name', 'description', 'food_price', 'quantity']
# courier_headers = ['courier_id', 'courier_name', 'courier_phone']
# customer_headers = ['customer_id','customer_name', 'customer_phone']
# customer_orders_headers = ['customer_id', 'order_id']
# product_orders_headers = ['order_id','product_id', 'quantity']
# orders_headers = ['order_id', 'courier_id', 'order_total']

cursor = database_func.open_db()
# sql = "INSERT INTO food (food_name, description,food_price,quantity) VALUES (%s,%s,%s,%s)"
# val = ('Salad', 'Chicken', 9.99, 100)
# cursor.execute(sql,val)
# database_func.close_db()

connection = get_connection()
cursor = connection.cursor()
cursor = database_func.open_db()
sql = "INSERT INTO food (product_id, food_name, description,food_price,quantity) VALUES (%s,%s,%s,%s,%s)"
val = (1,'Chocolate McChocolate Cake', "Cake that is chocolate, what more do you need to know", 20.00, 100)
cursor.execute(sql,val)
connection.commit()
cursor.close()
connection.close()



# food_name = input('What is it called?')
# food_description = input('Describe it?')
# database_func.add_to_db ('food' ,"food_name , description, food_price, quantity", f"'{food_name}', '{food_description}', '8.99', '100' ")

