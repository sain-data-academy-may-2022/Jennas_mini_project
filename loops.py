import menus
import database_func
from database_func import print_db
food_headers = ['product_id', 'Name', 'Description', 'Price']
courier_headers = ['courier_id', 'Name', 'Phone']
orders_headers = ['order_id', 'customer_name', 'customer_address', 'customer_phone', 'status', 'food', 'courier']

def food_loop(food_options):
    running = True
    if food_options == 0 :
        menus.Colour_red("FINE GO! Our Chocolate Cake is AMAZING, I'll get your money next time!'")
        running = False

    elif food_options == 1:
        database_func.print_db('food', food_headers )
                
    elif food_options == 2:
        food_name = menus.get_input('What is it called?')
        food_description = menus.get_input('Describe it?')
        database_func.add_to_db ('food' ,"Name , Description, Price", f"'{food_name}', '{food_description}', '1000' ")
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
  
def courier_loop (courier_options):
    running = True
    if courier_options == 0 :
        menus.Colour_red("Have a good day'")
        running = False

    elif courier_options== 1:
        database_func.print_db('couriers', courier_headers )
                
    elif courier_options == 2:
        courier_name = menus.get_input('What are they called?')
        courier_phone = menus.get_input_int('Their Number?')
        database_func.add_to_db ('couriers' ,"Name , Phone", f"'{courier_name}', '{courier_phone}' ")
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


def orders_loop (order_options):
    running = True
    if order_options == 0 :
        menus.Colour_red("Have a good day'")
        running = False

    elif order_options== 1:
        database_func.print_db('orders', orders_headers )
                
    elif order_options == 2:
        database_func.print_db('food', food_headers )
        database_func.add_to_order_db()
        database_func.print_db('orders', orders_headers )
        

    elif order_options== 3:
        database_func.print_db('orders', orders_headers )
        database_func.update_table('orders', 'order_id')
        database_func.print_db('orders', orders_headers )

    elif order_options == 4 :
        database_func.print_db('orders', orders_headers )
        database_func.delete_from_db('orders', 'order_id')
        database_func.print_db('orders', orders_headers )
                
    
    return running
    