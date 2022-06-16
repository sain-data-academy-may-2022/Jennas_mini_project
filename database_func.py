import pymysql
import os
from dotenv import load_dotenv
import random
from prettytable import PrettyTable
import menus

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

food_headers = ['product_id', 'food_name', 'description', 'food_price']
courier_headers = ['courier_id', 'courier_name', 'courier_phone']
orders_headers = ['order_id', 'customer_name', 'customer_address', 'customer_phone', 'status', 'food', 'courier']

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
    connection = get_connection()
    cursor = connection.cursor()
    id= menus.get_input_int('What ID do you want to update?')
    field = menus.get_input("What field do you want to change?")
    to = menus.get_input("to?")
    cursor.execute(f"""
    UPDATE {db_name}

    SET {field} ='{to}'

    WHERE {id_name} = {id} ;

    """)
    connection.commit()
    
     

def delete_from_db(db_name, id_name):
    delete_item = menus.get_input_int("what id?")
    cursor.execute(f"""
        DELETE FROM {db_name}

        WHERE {id_name} = '{delete_item}';

        """)
    connection.commit()
    


def delete_from_orders():
    
    delete_item = menus.get_input_int("what id?")
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


def select_last_id_for_input(id_name, db_name):
    cursor.execute(f"SELECT {id_name} FROM {db_name} WHERE {id_name}=(SELECT max({id_name}) FROM {db_name});")
    customer_id = cursor.fetchone()
    return customer_id
    
   