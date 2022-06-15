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

def open_db():
    connection = get_connection()
    cursor = connection.cursor()
    return cursor

def close_db():
    connection.commit()
    cursor.close()
    connection.close()

food_headers = ['product_id', 'Name', 'Description', 'Price']
courier_headers = ['courier_id', 'Name', 'Phone']
orders_headers = ['order_id', 'customer_name', 'customer_address', 'customer_phone', 'status', 'food', 'courier']

def print_db(db_name, headers):
    cursor.execute(f'Select * FROM {db_name}')
    rows = cursor.fetchall()
    x = PrettyTable()
    x.field_names = headers
    for row in rows:
        x.add_row(row)
    print(x)



#Food_inputs 



def add_to_db (db_name ,db_headings, values):
    cursor.execute(f"""
    INSERT INTO {db_name} ({db_headings})

    VALUES ({values});

    """)
    

def update_table (db_name, id_name):
    product_id= menus.get_input_int('What ID do you want to update?')
    field = menus.get_input("What field do you want to change?")
    to = menus.get_input("to?")
    cursor.execute(f"""
    UPDATE {db_name}

    SET {field} ='{to}'

    WHERE {id_name} = {product_id} ;

    """)

def delete_from_db(db_name, id_name):
    delete_item = menus.get_input_int("what id?")
    cursor.execute(f"""
        DELETE FROM {db_name}

        WHERE {id_name} = '{delete_item}';

        """)
    


def create_a_list_of_names_from_table(field_name,list_name):
    cursor.execute(f'SELECT {field_name} from {list_name};')
    rows = cursor.fetchall()
    my_list = rows
    return my_list

# courier_list =create_a_list_of_names_from_table('Name','couriers')

def add_to_order_db():
    select_food_choice = menus.get_input_int("What product_id do you want?")
    add_c_name = menus.get_input('Whats your name?')
    add_c_address = menus.get_input('Whats your address?')
    add_c_phone = menus.get_input_int('Whats your number?')
    cursor.execute(f"""
    SELECT Name

    FROM food

    WHERE product_id = {select_food_choice};""")
    food_choice = cursor.fetchall()
    add_courier = random.choice(courier_list)
    new_order = [add_c_name, add_c_address, add_c_phone, 'Preparing', food_choice, add_courier]
    sql = "INSERT INTO orders (customer_name, customer_address, customer_phone, status,food,courier) VALUES (%s, %s, %s, %s, %s, %s);" 
    val = (new_order)
    cursor.execute(sql, val)
    