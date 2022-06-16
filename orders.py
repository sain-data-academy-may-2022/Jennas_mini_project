import database_func 
from prettytable import PrettyTable
import menus
import random



def add_to_order():
    food_headers = ['product_id', 'food_name', 'description', 'food_price', 'quantity']

    connection = database_func.get_connection()
    cursor = connection.cursor()

#Add to customer db
    add_c_name = menus.get_input('Whats your name?')
    add_c_address = menus.get_input('Whats your address?')
    add_c_phone = menus.get_input_int('Whats your number?')
    sql = ("INSERT INTO customers (customer_name, customer_address, customer_phone) VALUES (%s, %s, %s)")
    val = (f"{add_c_name}", f"{add_c_address}", add_c_phone)
    cursor.execute(sql,val)

#GET customer id for customer_orders db
    cursor.execute("SELECT customer_id FROM customers WHERE customer_id=(SELECT max(customer_id) FROM customers);")
    customer_id = cursor.fetchone()

# Add to customer_orders db
    sql = ("INSERT INTO customer_orders (customer_id) VALUES (%s)")
    val = (customer_id)
    cursor.execute(sql,val)
    connection.commit()

#Print food table so we can get an order
    database_func.print_db('food', food_headers )

#Get order_id for food_orders
    cursor.execute("SELECT order_id FROM customer_orders WHERE order_id=(SELECT max(order_id) FROM customer_orders);")
    order_id = cursor.fetchone()

#Loop so they can order as much as they want
    while(True):
# Mini Loop to check if item is in stock        
        while(True):
            product_id1 = int(input("What product id would you like to order?"))
            cursor.execute(f'SELECT quantity from food WHERE product_id = {product_id1};')
            fetch = cursor.fetchall()
            out_of_stock = int(fetch[0][0])
            if out_of_stock == 0:
                print("Sorry thats out of stock, order something else")
            if not out_of_stock == 0:
                break
        quantity1= int(input("How many? "))

#Work out the price for food_orders table
        cursor.execute(f"SELECT food_price * {quantity1} as TOTAL FROM food WHERE product_id= {product_id1};")
        price1 = cursor.fetchall()

#add to food_orders db
        sql =('INSERT INTO food_orders (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)')
        val = (order_id, product_id1, quantity1, price1)
        cursor.execute(sql,val)

#Work out new quantity in food table
        cursor.execute(f"SELECT quantity - {quantity1} as TOTAL FROM food WHERE product_id= {product_id1};")
        newquantity= cursor.fetchall()
        cursor.execute(f"""
        UPDATE food

        SET quantity ='{int(newquantity[0][0])}'

        WHERE product_id= {product_id1};

        """)
        connection.commit()

#Add more item to order
        more = input("Do you want to order anything else, y or n?")
        if more == "n":
            print("""
                
Alright, thank you for your small amount of money, hope you stay hungry.
                
                
                """)
#Get order_id      
            cursor.execute("SELECT order_id FROM customer_orders WHERE order_id=(SELECT max(order_id) FROM customer_orders);")
            order_id = cursor.fetchone()

#Get random courier
            cursor.execute('SELECT courier_id from couriers;')
            rows = cursor.fetchall()
            courier_list = rows
            courier_id= random.choice(courier_list)

#Work out total price
            cursor.execute(f"""SELECT SUM(price) FROM food_orders
            WHERE order_id = ({int(order_id[0])});
            """)
            total_price = cursor.fetchall()

#Add to orders db
            sql =('INSERT INTO orders (order_id, courier_id,total_price) VALUES (%s, %s, %s)')
            val = (order_id, courier_id, total_price)
            cursor.execute(sql,val)
            connection.commit()
            break
        if more == "y":
            print("")