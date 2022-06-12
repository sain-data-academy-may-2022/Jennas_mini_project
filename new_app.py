import database_func
import password
import menus
import loops


while(True):
    menus.Colour_red(""" 
                          ---- Costa'lot ---- 
                                

(0) To exit app.
(1) Food Menu
(2) Couriers Menu
(3) Orders Menu

                                --------------------""")
    menu = int(input())
    if menu == 0:
        print("See you never!")
        database_func.close_db()
        break

    
    menu_1 = True
    while (menu_1):
        if menu == 1:
            database_func.open_db()
            menus.print_menu(menus.food_menu)
            food_options = menus.get_input_int("Hurry up and pick something would you?")
            menu_1 = loops.food_loop(food_options)

        else:
            break
        
 
    menu_2 = True
    while (menu_2):
        if menu == 2:
            database_func.open_db()
            menus.print_menu(menus.couries_menu)
            courier_options = menus.get_input_int("What do you want to do with these idiots?")
            menu_2 = loops.courier_loop(courier_options)
        
        else:
            break


    menu_3 = True
    while (menu_3):
        if menu == 3:
            database_func.open_db()
            menus.print_menu(menus.orders_menu)
            order_options = menus.get_input_int("You best be adding an order, we need that money!?")
            menu_3 = loops.orders_loop(order_options)
        
        else:
            break
                    
    
    
