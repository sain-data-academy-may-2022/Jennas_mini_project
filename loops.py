from itertools import product
import menus
import database_func
from database_func import print_db
import orders
food_headers = ['product_id', 'food_name', 'description', 'food_price', 'quantity']
courier_headers = ['courier_id', 'courier_name', 'courier_phone']
orders_headers = ['order_id', 'courier_id', 'total_price', 'status']
customer_headers = ['customer_id', 'customer_name', 'customer_address', 'customer_phone']

#food 

def food_loop(food_options):
    running = True
    if food_options == 0 :
        menus.Colour_red("""
        
 Our Chocolate Cake is AMAZING, I'll get your money next time! Enter 0 to exit the app.
 
 """)
        running = False

    elif food_options == 1:
        database_func.print_db('food', food_headers )
                
    elif food_options == 2:
        food_name = menus.get_input('What is it called?')
        food_description = menus.get_input('Describe it?')
        database_func.add_to_db ('food' ,"food_name , description, food_price, quantity", f"'{food_name}', '{food_description}', 1000.00, 100 ")
        database_func.print_db('food', food_headers )
        
        

    elif food_options == 3:
        database_func.print_db('food', food_headers )
        database_func.update_table('food', 'product_id')
        database_func.print_db('food', food_headers )

    elif food_options == 4 :
        database_func.print_db('food', food_headers )
        database_func.delete_from_db('food', 'product_id')
        database_func.print_db('food', food_headers )
                
    
    return running

#customer
def customers_loop (customer_options):
    running = True
    if customer_options == 0 :
        menus.Colour_red("""
        
Card better not bounce!
""")
        running = False

    elif customer_options== 1:
        database_func.print_db('customers', customer_headers )
                
    elif customer_options == 2:
        add_c_name = menus.get_input('Whats your name?')
        add_c_address = menus.get_input('Whats your address?')
        add_c_phone = menus.get_input_int('Whats your number?')
        database_func.add_to_db ('customers' ,"customer_name, customer_address, customer_phone", f"'{add_c_name}', '{add_c_address}', '{add_c_phone}' ")
        database_func.print_db('customers', customer_headers )
        

    elif customer_options== 3:
        database_func.print_db('customers', customer_headers )
        database_func.update_table('customers', 'customer_id')
        database_func.print_db('customers', customer_headers )

    elif customer_options == 4:
        database_func.print_db('customers', customer_headers )
        database_func.delete_from_customers()
        database_func.print_db('customers', customer_headers )

    return running
    
#orders 
def orders_loop (order_options):
    running = True
    if order_options == 0 :
        menus.Colour_red("""

Good Job. Remember our motto 'Take what you can, give minimal back ^_^' """

)
        running = False

    elif order_options== 1:
        database_func.print_db('orders', orders_headers )
                
    elif order_options == 2:
        database_func.print_db('food', food_headers )
        orders.add_to_order()
        database_func.print_db('orders', orders_headers )
        

    elif order_options== 3:
        database_func.print_db('orders', orders_headers )
        database_func.update_table('orders', 'order_id')
        database_func.print_db('orders', orders_headers )


    elif order_options == 4:
        search = menus.get_input("""


Do you want to search by status or courier?
""")
        if search == "status":
            database_func.search_by_key("""
See Delivered or Preparing?""", 'status', 'orders', ('order_id', 'status'))
        if search == "courier":
            database_func.print_db('couriers', courier_headers )
            database_func.search_by_key('Which courier do you want check up on? ', 'courier_id', 'orders', ('order_id', 'courier_id'))

    elif order_options == 5:
        database_func.print_specific_db('food', 'food_name , quantity', ['food_name', 'quantity'])
             

    elif order_options == 6:
        database_func.print_db('orders', orders_headers )
        database_func.delete_from_orders()
        database_func.print_db('orders', orders_headers )
                
    
    return running


 #couriers 
def courier_loop (courier_options):
    running = True
    if courier_options == 0 :
        menus.Colour_red("""

laters...""")
        running = False

    elif courier_options== 1:
        database_func.print_db('couriers', courier_headers)
                
    elif courier_options == 2:
        courier_name = menus.get_input('What are they called?')
        courier_phone = menus.get_input_int('Their Number?')
        database_func.add_to_db ('couriers' ,"courier_name , courier_phone", f"'{courier_name}', '{courier_phone}' ")
        database_func.print_db('couriers', courier_headers )
        

    elif courier_options== 3:
        database_func.print_db('couriers', courier_headers )
        database_func.update_table('couriers', 'courier_id')
        database_func.print_db('couriers', courier_headers )

    elif courier_options == 4 :
        database_func.print_db('couriers', courier_headers )
        database_func.delete_from_db('couriers', 'courier_id')
        database_func.print_db('couriers', courier_headers )
                
    
    return running





