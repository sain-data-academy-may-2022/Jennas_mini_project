import database_func 
from prettytable import PrettyTable
import menus
import random



def add_to_order():
    food_headers = ['product_id', 'food_name', 'description', 'food_price', 'quantity']

    connection = database_func.get_connection()
    cursor = connection.cursor()

    add_c_name = menus.get_input('Whats your name?')
    add_c_address = menus.get_input('Whats your address?')
    add_c_phone = menus.get_input_int('Whats your number?')
    sql = ("INSERT INTO customers (customer_name, customer_address, customer_phone) VALUES (%s, %s, %s)")
    val = (f"{add_c_name}", f"{add_c_address}", add_c_phone)
    cursor.execute(sql,val)
    cursor.execute("SELECT customer_id FROM customers WHERE customer_id=(SELECT max(customer_id) FROM customers);")
    customer_id = cursor.fetchone()
    sql = ("INSERT INTO customer_orders (customer_id) VALUES (%s)")
    val = (customer_id)
    cursor.execute(sql,val)
    connection.commit()
    cursor.execute(f'Select * FROM food')
    rows = cursor.fetchall()
    x = PrettyTable()
    x.field_names = food_headers
    for row in rows:
        x.add_row(row)
    print(x)
    cursor.execute("SELECT order_id FROM customer_orders WHERE order_id=(SELECT max(order_id) FROM customer_orders);")
    order_id = cursor.fetchone()
    while(True):
        connection = database_func.get_connection()
        cursor = connection.cursor()
        product_id1 = int(input("What product id would you like to order?"))
        cursor.execute(f'SELECT quantity from food WHERE product_id = {product_id1};')
        fetch = cursor.fetchall()
        out_of_stock = int(fetch[0][0])
        print(out_of_stock)
        if out_of_stock == 0:
            print("Sorry thats out of stock, order something else")
        if not out_of_stock == 0:
            break
    quantity1= int(input("How many? "))
    cursor.execute(f"SELECT food_price * {quantity1} as TOTAL FROM food WHERE product_id= {product_id1};")
    price1 = cursor.fetchall()
    sql =('INSERT INTO food_orders (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)')
    val = (order_id, product_id1, quantity1, price1)
    cursor.execute(sql,val)
    cursor.execute(f"SELECT quantity - {quantity1} as TOTAL FROM food WHERE product_id= {product_id1};")
    newquantity= cursor.fetchall()
    cursor.execute(f"""
    UPDATE food

    SET quantity ='{int(newquantity[0][0])}'

    WHERE product_id= {product_id1};

    """)
    connection.commit()


    while(True):

        more = input("Do you want to order anything else, yes or no?")
        if more == "n":
            print("""
            
Alright, thank you for your small amount of money, hope you stay hungry.
            
            
            """)
            cursor.execute("SELECT order_id FROM customer_orders WHERE order_id=(SELECT max(order_id) FROM customer_orders);")
            order_id = cursor.fetchone()
            cursor.execute(f"""SELECT SUM(price) FROM food_orders
            WHERE order_id = ({int(order_id[0])});
            """)
            total_price = cursor.fetchall()
            cursor.execute('SELECT courier_id from couriers;')
            rows = cursor.fetchall()
            courier_list = rows
            courier_id= random.choice(courier_list)
            sql =('INSERT INTO orders (order_id, courier_id,total_price) VALUES (%s, %s, %s)')
            val = (order_id, courier_id, total_price)
            cursor.execute(sql,val)
            connection.commit()
            break
        if more == "y":
            cursor.execute("SELECT order_id FROM customer_orders WHERE order_id=(SELECT max(order_id) FROM customer_orders);")
            order_id = cursor.fetchone()
            while(True):
                connection = database_func.get_connection()
                cursor = connection.cursor()
                product_id2 = int(input("What product id would you like to order?"))
                cursor.execute(f'SELECT quantity from food WHERE product_id = {product_id2};')
                fetch = cursor.fetchall()
                out_of_stock = int(fetch[0][0])
                print(out_of_stock)
                if out_of_stock == 0:
                    print("Sorry thats out of stock, order something else")
                if not out_of_stock == 0:
                    break
            quantity2= int(input("How many? "))
            cursor.execute(f"SELECT food_price * {quantity2} as TOTAL FROM food WHERE product_id= {product_id2};")
            price2 = cursor.fetchall()
            sql =('INSERT INTO food_orders (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)')
            val = (order_id, product_id2, quantity2, price2)
            cursor.execute(sql,val)
            cursor.execute(f"SELECT quantity - {quantity2} as TOTAL FROM food WHERE product_id= {product_id2};")
            newquantity= cursor.fetchall()
            cursor.execute(f"""
            UPDATE food

            SET quantity ='{int(newquantity[0][0])}'

            WHERE product_id= {product_id2};

            """)
            connection.commit()
            
             



