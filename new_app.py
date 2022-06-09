from csv_func import add_to_order_csv, save_to_csv, open_a_csv, add_to_order_csv, update_order_status_csv, delete_order_from_csv
from Colour import Colour_red
from database_func import print_food_table, get_connection, close_connection, print_courier_table, add_food, update_food_table, delete_from_food_table
from list_func import add_to_a_list, print_nice_order_list
# import random

# my_lists so functions can access
food_list = open_a_csv('new_food', 'food_list' )
courier_list = open_a_csv('new_couriers', 'courier_list' )
order_list = open_a_csv('new_orders', 'order_list' )

#my_headers
food_headers = ['product_id', 'Food Name', 'Description', 'Price']
courier_headers = ['Name', 'Phone']
orders_headers = ['order_id', 'customer_name', 'customer_address', 'customer_phone', 'status', 'food', 'courier']


while(True):
    Colour_red(""" 
                          ---- Costa'lot ---- 
                                

(0) To exit app.
(1) Food Menu
(2) Couriers Menu
(3) Orders Menu

                                --------------------""")

    menu = int(input())
    if menu == 0:
        save_to_csv('new_food', food_headers, food_list)
        save_to_csv('new_couriers', courier_headers, courier_list)
        save_to_csv('new_orders', orders_headers,  order_list)
        break

    elif menu == 1:
        while(True):
            choice =  int(input("""

(0) Imma head out.
(1) See the menu!!!!
(2) I'm a princess make something special?
(3) Close, but you want to mix it up a litte?
(4) Get rid of that!

Hurry up and pick something would you?
            
            """)) 

            if choice == 0 :
                Colour_red("FINE GO! Our Chocolate Cake is AMAZING, I'll get your money next time!'")
                break


# Created database_func as a module to hold all database functions
            elif choice == 1:
                print_food_table()
                     
            elif choice == 2:
                add_food()
  
            elif choice == 3:
                update_food_table()
               
        
            elif choice == 4 :
                delete_from_food_table()
                
                    
    elif menu == 2:
        while(True):
            courier_options = int(input("""
Couriers Menu  
         (0) Exit
         (1) Show current couriers names
         (2) Add Courier
         (3) Update a couriers details. 
         (4) Delete a courier."""))
            
            if courier_options == 0:
                break
            
            elif courier_options == 1:
                print_courier_table()
    
                
                
               
            elif courier_options == 2:
                new_name = input("What's the name? They best not be some idiot on a bike!")
                new_phone = input("And their number?")
                add_courier_name = [new_name, new_phone]
                 # In list_func module  
                add_to_a_list(courier_list,add_courier_name)
                connection = get_connection()
                cursor = connection.cursor()
                sql = "INSERT INTO couriers (Name, Phone) VALUES (%s, %s)" 
                val = (add_courier_name)
                cursor.execute(sql, val)
                connection.commit()
                cursor.close()
                close_connection(connection)
                print_courier_table()

# USE DATABASE TO PULL IN PRODUCTS     
            elif courier_options == 3:
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


            elif courier_options == 4 :
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



    elif menu == 3:
        while(True):
            order_options = int(input("""Orders Menu  

(0) Exit
(1) Show current orders? 
(2) Add an order?
(3) Update a order details? 
(4) Delete an order?"""))

            if order_options == 0:
                # In database_func module
                save_to_csv('new_orders', orders_headers, order_list)
                break

            if order_options == 1:
                # In list_func module 
                print_nice_order_list(order_list)

            if order_options == 2:
                add_to_order_csv(order_list,food_list,courier_list)
                

            if order_options == 3:
                update_order_status_csv(order_list)

            if order_options == 4:
                delete_order_from_csv(order_list)
                





                
                   







            




