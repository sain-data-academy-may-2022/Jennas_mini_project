import pymysql
courier_headers = ['courier_id', 'courier_name', 'courier_phone']

def int_input(your_text):
    global menu
    try:
        menu = int(input(your_text))
    except:
        print("I need a number!")
        int_input("Try again, idiot?! ")
    
    return menu

def update_table_input(cursor, connection, db_name, id_name):
    try:
        id= int_input('What ID do you want to update?')
        field = input("What field do you want to change?")
        to = input("to?")
        cursor.execute(f"""
        UPDATE {db_name}

        SET {field} ='{to}'

        WHERE {id_name} = {id} ;

        """)
        connection.commit()
    
    except pymysql.err.ProgrammingError:
        print("You messed up somewhere, try again")
        update_table_input(cursor, connection,db_name, id_name)

    except pymysql.err.OperationalError:
        print("You messed up somewhere, try again")
        update_table_input(cursor, connection,db_name, id_name)
        
    except pymysql.err.DatabaseError:
        print("You messed up somewhere, try again")
        update_table_input(cursor, connection,db_name, id_name)

def delete_from_table(cursor, connection, db_name, id_name):
    try:
        delete_item = int_input("what id do you want to delete?")
        cursor.execute(f"""
            DELETE FROM {db_name}

            WHERE {id_name} = '{delete_item}';

            """)
        connection.commit()
        print("All gone! Happy now?")
    except:
        print("You messed up somewhere, try again")
        delete_from_table(cursor, connection, db_name, id_name)

 
def how_many(out_of_stock):
    quantity1= int(input("How many? "))
    if quantity1 > out_of_stock:
        print("Stop being greedy, we don't have that many")
        how_many(out_of_stock)
    if quantity1 < out_of_stock:
        print("Great we have enough")

      
def stock_check(out_of_stock):
    while(True):
        my_order =int_input("how many would you like?")
        if my_order < out_of_stock: 
            print('Yup, we can do that!')
            new_stock = my_order
            return new_stock
        if my_order > out_of_stock:
            print('Oi greedy, we dont have enough!')


def real_product(cursor):
    while(True):
        product_id1 = int_input("What product id would you like to order?")
        cursor.execute(f'SELECT quantity from food WHERE product_id = {product_id1};')
        fetch = cursor.fetchall()
        global the_fetch
        try:
            the_fetch = (fetch[0][0])
            product_id2 = product_id1
            return product_id2
        except IndexError:
            print("An actual product please!")
            
    


