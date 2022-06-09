import pymysql
import os
from dotenv import load_dotenv
from csv_func import save_to_csv

#Access Database

load_dotenv()
my_host = os.environ.get("mysql_host")
my_user = os.environ.get("mysql_user")
my_password = os.environ.get("mysql_pass")
my_database = os.environ.get("mysql_db")

 
def get_connection():   
    my_connection = pymysql.connect(
    host=my_host,
    user=my_user,
    password=my_password,
    database=my_database
    )
    return my_connection

def close_connection(connection):
    connection.close()

#My database functions 

#FOOD functions

#open/print food table
def print_food_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * from food')
    rows = cursor.fetchall()
    for row in rows:
        print (row[0],f'{row[1]}:', row[2], f'£{row[3]}')
    cursor.close()
    close_connection(connection)

#Add food to table 

def add_food():
    new_name = input("Alright princess, What special dish can your slave make for you?")
    new_description = input("Any particular type your highness?")
    add_food_name = [new_name, new_description, 1000]
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO food (Food_Name, Description, Price) VALUES (%s, %s, %s)" 
    val = (add_food_name)
    cursor.execute(sql, val)
    connection.commit()
    cursor.close()
    close_connection(connection)
    print_food_table()

#Update an item in food table

def update_food_table():
    connection = get_connection()
    cursor = connection.cursor()
    print_food_table()
    select_product_id = input("what do you want to update?")
    cursor.execute(f"""
    SELECT *

    FROM food

    WHERE product_id = {select_product_id}""")
    what_update = input("What bit do you want to update Food_Name or Description?")
    update_to = input("to?")
    cursor.execute(f""" 
    UPDATE food

    SET
    {what_update} = '{update_to}'

    WHERE product_id = {select_product_id}; 

    """)
    connection.commit()
    cursor.close()
    close_connection(connection)
    print_food_table()

# DELETE ITEM FROM FOOD TABLE
def delete_from_food_table():
    connection = get_connection()
    cursor = connection.cursor()
    print_food_table()
    delete_item = input("What do you want to delete?")
    cursor.execute(f"""
    DELETE FROM food
    
    WHERE product_id = {delete_item};
    """)
    connection.commit()
    cursor.close()
    close_connection(connection)
    print_food_table()



#Courier functions





def print_courier_table():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * from couriers')
    rows = cursor.fetchall()
    for row in rows:
        print (row[0],row[1],row[2])
    cursor.close()
    close_connection(connection)


def add_to_courier_table():
    new_name = input("What's the name? They best not be some idiot on a bike!")
    new_phone = input("And their number?")
    add_courier_name = [new_name, new_phone]
    connection = get_connection()
    cursor = connection.cursor()
    sql = "INSERT INTO couriers (Name, Phone) VALUES (%s, %s)" 
    val = (add_courier_name)
    cursor.execute(sql, val)
    connection.commit()
    cursor.close()
    close_connection(connection)
    print_courier_table()

def update_to_courier_table():
    connection = get_connection()
    cursor = connection.cursor()
    print_courier_table()
    select_row = input("Which one do you want to update?")
    cursor.execute(f"""
    SELECT *

    FROM couriers

    WHERE courier_id = {select_row}""")
    what_update = input("What bit do you want to update Name or Phone?")
    update_to = input("to?")
    cursor.execute(f""" 
    UPDATE couriers

    SET
    {what_update} = '{update_to}'

    WHERE courier_id = {select_row}; 

    """)
    connection.commit()
    cursor.close()
    
    close_connection(connection)
    print_courier_table()

def delete_from_courier_table():
    connection = get_connection()
    cursor = connection.cursor()
    print_courier_table()
    delete_item = input("What do you want to delete?")
    cursor.execute(f"""
    DELETE FROM couriers
    
    WHERE courier_id = {delete_item};
    """)
    connection.commit()
    cursor.close()
    close_connection(connection)
    print_courier_table()





def create_a_list():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute('SELECT * from food')
    rows = cursor.fetchall()
    my_list = rows
    return my_list












