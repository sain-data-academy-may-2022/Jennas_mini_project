import database_func
import menus
import loops
import inputs


while(True):
    database_func.open_db()
    menus.Colour_red(""" 
                          £££ ---- Costa'lot ---- £££
                                

(0) To exit app.
(1) Food Menu
(2) Orders Menu
(3) Couriers Menu
(4) Customers Menu

                             --------------------""")
    
    menu = inputs.int_input('')
    if menu == 0:
        print("See you never!")
        database_func.close_db()
        break

#First Loop   
#Food Menu 
    menu_1 = True
    while (menu_1):
        if menu == 1:
            database_func.open_db()
            menus.print_menu(menus.food_menu)
            food_options = inputs.int_input("""

Hurry up and pick something would you!

""")
            menu_1 = loops.food_loop(food_options)

        else:
            break
        
 #Orders Menu 
    menu_2 = True
    while (menu_2):
        if menu == 2:
            database_func.open_db()
            menus.print_menu(menus.orders_menu)
            order_options = inputs.int_input("""

You best be adding an order, we need that money!?
""")
            menu_2 = loops.orders_loop(order_options)
        
        else:
            break

#Couriers Menu 
    menu_3 = True
    while (menu_3):
        if menu == 3:
            database_func.open_db()
            menus.print_menu(menus.couriers_menu)
            courier_options = inputs.int_input("""
            

What do you want to do with these idiots?
""")
            menu_3 = loops.courier_loop(courier_options)
        
        else:
            break
#Customer Menu 
    menu_4 = True
    while (menu_4):
        if menu == 4:
            database_func.open_db()
            menus.print_menu(menus.customer_menu)
            customer_options = inputs.int_input("""
If you're deleting any money, I mean a customer, you're fired!
""")
            menu_4 = loops.customers_loop(customer_options)
        
        else:
            break
                    
    
    
