import database_func 
from prettytable import PrettyTable
import inputs

food_headers = ['product_id', 'food_name', 'description', 'food_price', 'quantity']

connection = database_func.get_connection()
cursor = connection.cursor()

def add_to_order():
    customer_id=database_func.add_customer()
   

# Add to customer_orders db
    database_func.add_to_db_val('customer_orders', 'customer_id', '%s', customer_id) 
    

#Print food table so we can get an order
    database_func.print_db('food', food_headers)

#Get order_id needed for food_orders
    cursor.execute("SELECT order_id FROM customer_orders WHERE order_id=(SELECT max(order_id) FROM customer_orders);")
    order_id = cursor.fetchone()
    

#Loop so they can order as much as they want
    while(True):
# Mini Loop to check if item is in stock        
        while(True):
            product_id1 = inputs.real_product(cursor)
            cursor.execute(f'SELECT quantity from food WHERE product_id = {product_id1};')
            fetch = cursor.fetchall()
            out_of_stock = int(fetch[0][0])
            if out_of_stock == 0:
                print("Sorry thats out of stock, order something else")
            if not out_of_stock == 0:
                break
        quantity1 = inputs.stock_check(out_of_stock)
            

#Work out the price for food_orders table
        price1 = database_func.work_out_price(quantity1, product_id1)
    
#take all info add food_orders db
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
        answers = ['y', 'n']
        more = None
        while more not in answers:
            more = input('Do you want to order anything else, y or n? ')
        if more == "n":
            print("""
                
Alright, thank you for your small amount of money, hope you stay hungry.
                
                
                """)

# Get information for the orders tab


#Get order_id      
            cursor.execute("SELECT order_id FROM customer_orders WHERE order_id=(SELECT max(order_id) FROM customer_orders);")
            order_id = cursor.fetchone()

#Get random courier
            courier_id = database_func.random_choice_from_db('courier_id', 'couriers')

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

