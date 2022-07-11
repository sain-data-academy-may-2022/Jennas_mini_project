from operator import add
from string import printable
from numpy import int64
import pymysql
import os
from dotenv import load_dotenv
import random
from prettytable import PrettyTable
import menus
import inputs


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

#open/close functions for db

def open_db():
    connection = get_connection()
    cursor = connection.cursor()
    return cursor

def close_db():
    connection.commit()
    cursor.close()
    connection.close()

def execute_db(do_it):
    cursor.execute(do_it)
    connection.commit()


food_headers = ['product_id', 'food_name', 'description', 'food_price']
courier_headers = ['courier_id', 'courier_name', 'courier_phone']
orders_headers = ['order_id', 'courier_id', 'total_price', 'status']

# print everything in the database
def print_db(db_name, headers):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(f'Select * FROM {db_name}')
    rows = cursor.fetchall()
    x = PrettyTable()
    x.field_names = headers
    for row in rows:
        x.add_row(row)
    print(x)

# print specific keys the database
def print_specific_db(db_name, keys, headers):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(f'Select {keys} FROM {db_name}')
    rows = cursor.fetchall()
    x = PrettyTable()
    x.field_names = headers
    for row in rows:
        x.add_row(row)
    print(x)



#basic funcs add/update/delete db - work for all but orders

def add_to_db (db_name ,db_headings, values):
    cursor.execute(f"""
    INSERT INTO {db_name} ({db_headings})

    VALUES ({values});

    """)
    connection.commit()
 

def update_table (db_name, id_name):
    inputs.update_table_input(cursor, connection,db_name, id_name)
    
     

def delete_from_db(db_name, id_name):
    cursor.execute('SET FOREIGN_KEY_CHECKS=0')
    inputs.delete_from_table(cursor, connection, db_name, id_name)
    


def delete_from_orders():
    
    delete_item = inputs.int_input("what id do you want to delete?")
    cursor.execute(f"""
    DELETE FROM orders WHERE order_id = {delete_item};

    """)
    cursor.execute(f"""
    DELETE FROM food_orders WHERE order_id = {delete_item};

    """)
    cursor.execute(f"""
    DELETE FROM customer_orders WHERE order_id = {delete_item};

    """)
    connection.commit()

def delete_from_customers():
    delete_item = menus.get_input_int("what id?")
    cursor.execute('SET FOREIGN_KEY_CHECKS=0')
    cursor.execute(f"""
    DELETE FROM customer_orders 

    WHERE customer_id ={delete_item};

    """)
    cursor.execute(f"""
    DELETE FROM customers 


    WHERE customer_id = {delete_item};

    """)
    connection.commit()



#search by delivery status or courier     
def search_by_key(value_question: str, key_choice, database_name, headers):
    connection = get_connection()
    cursor = connection.cursor()
 # Delivered or Prearing/ What courier ?  
    status = input(value_question) 
    cursor.execute(f"SELECT order_id, {key_choice} FROM {database_name} WHERE {key_choice} = '{status}';")
    status_list = cursor.fetchall()
    x = PrettyTable()
    x.field_names = headers
    for row in status_list:
        x.add_row(row)
    print(x)

#select last id - need to refractor in - grabs last id - customer_id - orders for example
def select_last_id_for_input(id_name, db_name):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT {id_name} FROM {db_name} WHERE {id_name}=(SELECT max({id_name}) FROM {db_name});")
    customer_id = cursor.fetchone()
    return customer_id

#adding to a database - using values %s 
def add_to_db_val(db_name, id_name, number_s, values):
    sql = (f"INSERT INTO {db_name} ({id_name}) VALUES ({number_s})")
    val = (values)
    try:
        cursor.execute(sql,val)
        connection.commit()
    except pymysql.err.IntegrityError:
        print ("")
        


#random choice used for the couriers atm - but could be used for any database
def random_choice_from_db(id_name, db_name):
    cursor.execute(f'SELECT {id_name} from {db_name};')
    rows = cursor.fetchall()
    list = rows
    random_id= random.choice(list)
    return random_id


###JOINS to print mixed tables - for users 

#orders 

def orderdb_id_name_price_status():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute( """SELECT customer_orders.order_id, customers.customer_id, customers.customer_name, orders.total_price, orders.status
                        
                        FROM customer_orders
                        INNER JOIN customers ON customer_orders.customer_id=customers.customer_id
                        INNER JOIN orders on customer_orders.order_id=orders.order_id;""")
    rows = cursor.fetchall()
    x = PrettyTable()
    x.field_names = ['order_id', 'customer_id', 'customer_name', 'total_price', 'status']
    for row in rows:
        x.add_row(row)
    print(x)

def orderdb_name_food():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute( """SELECT food_orders.order_id, customers.customer_name, food.food_name
                        
                        FROM food_orders
                        INNER JOIN food ON food_orders.product_id=food.product_id
                        INNER JOIN customer_orders ON food_orders.order_id = customer_orders.order_id
                        INNER JOIN customers ON customer_orders.customer_id=customers.customer_id
                        
                        ORDER BY order_id""")
    rows = cursor.fetchall()
    x = PrettyTable()
    x.field_names = ['order_id', 'customer_name', 'food_name']
    for row in rows:
        x.add_row(row)
    print(x)












# adding customer //checking id 
def add_customer():
    global customer_id
    existing_id = inputs.int_input("""


Do you have a customer id? 
Enter it if you do, otherwise enter 0? 
    
    """)
    if existing_id >= 1:
        try:
            
            cursor.execute(f"SELECT customer_name FROM customers WHERE customer_id={existing_id}")
            name = cursor.fetchone()
            print(f"""

Welcome back, {name[0]}

""")
            customer_id = existing_id
            return customer_id
        except TypeError:
            print ("You aren't a customer! You can't fool us!")
            add_customer()

    if existing_id == 0:
        #Add to customer db
        cursor.execute("SELECT customer_address FROM customers")
        address_list = [i[0] for i in cursor.fetchall()]

        cursor.execute("SELECT customer_phone FROM customers")
        phone_list = [i[0] for i in cursor.fetchall()]

        add_c_name = menus.get_input('Whats your name?')
        add_c_address = menus.get_input('Whats your address?')
        add_c_phone = inputs.phone_input()
        if add_c_address in address_list and add_c_phone in phone_list:
            cursor.execute(f"SELECT customer_id FROM customers WHERE customer_address = '{add_c_address}' AND customer_phone = '{add_c_phone}'")
            fetch= cursor.fetchall()[0]
            customer_id =fetch[0]
            print(f"You've ordered before! Your customer_id is {customer_id}")
            add_customer()
        else:
            add_to_db('customers', "customer_name, customer_address, customer_phone", f"'{add_c_name}', '{add_c_address}', '{add_c_phone}'")
            cursor.execute("SELECT customer_id FROM customers WHERE customer_id=(SELECT max(customer_id) FROM customers);") 
            customer_id = cursor.fetchone()
            return customer_id

    return customer_id


#work out a price 
def work_out_price(quantity:int, product_id: int):
    cursor.execute(f"SELECT food_price * {quantity} as TOTAL FROM food WHERE product_id= {product_id};")
    price1 = cursor.fetchall()
    return price1













#'search' order status/courier
def status_or_courier():
    search = input('Do you want to search by status or courier?')
    if search == "status":
        search_by_key("""
See Delivered or Preparing?""", 'status', 'orders', ('order_id', 'status'))
    if search == "courier":
        print_db('couriers', courier_headers )
        search_by_key('Which courier do you want check up on? ', 'courier_id', 'orders', ('order_id', 'courier_id'))

    else:
        print('STATUS OR COURIER!')
        status_or_courier()

    






    







