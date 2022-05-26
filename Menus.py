from password import password
from orders import order_system_fun
from courier_system import Courier_list_fun
from logins import logins_list_fun
from Colour import Colour_red
from Food import add_order_george, food_list, food_order, show_food_options, show_food_option_nums

product = {
    '1' : '(0) Imma head out ',
    '1' : '(1) See the menu!!!!',
    '2' : "(2) I'm a princess make something special?",
    '3' : '(3) Close, but you want to mix it up a litte?',
    '4' : '(4) Get rid of that',
}          
    
def backend():
    
    password()
    managers_menu = input ("""
    
You're the best! What do you want to do with these numptys orders? 
(0) Go to the order system
(1) Go to the courier system
(2) Go to the account system
    
    """
    )
    if (managers_menu == '0'):
        order_system_fun()
            
    elif (managers_menu == '1'):
        Courier_list_fun()

    elif (managers_menu== '2'):
        logins_list_fun()

       
#AND WE"RE DONE WITH THE FUNCTIONS!! Now time for the main event "The actual code"
def Main_menu():
    while(True):
        Colour_red(""" 
                                    ---- Costa'lot ---- 
                                    

    (0) To exit app.
    (1) To see our food options and place an order.
    (2) For the governer only (Do you know the magic word? If not don't even try it!)""")

        menu = input()
        if (menu == '0') or (menu == 'no'):
            Colour_red("FINE GO! Our Chocolate Cake is AMAZING, I'll get your money next time!'") 
            break

        if (menu == '1') or (menu == 'yes'):
            for key, value in product.items() :
                    print(value)
            choice =  (input("""
    Hurry up and pick something would you?
            
            """)) 

            if (choice == '1'):
                add_order_george()
                break

            elif (choice == '2'):
                custom = input("""
    Alright princess, What special dish can your slave make for you?""")
                describe = input (
    """Any particular type your highness?""")
                food_list.append(custom)
                custom_1 = (f"{custom}: {describe}")
                food_order[5] = custom_1 
                add_order_george()
                break
                
                    
            elif (choice == '3'):
                show_food_options()
                print(("""Alright Boss, what do you want to change?
                """))
                update_item= input ()
                item_change = input('Just remeber your own ideas cost more, but what is it?')
                item_description = input('In more detail please?!?!')
                item_1 = (f"{item_change}: {item_description}")
                food_order[update_item] = item_1
                show_food_options()
                add_order_george()
                break
                

            elif (choice == '4'):
                show_food_option_nums()
                print("""
    Alright miserable, what do you want to delete?""")
                delete_item= int(input())
                if delete_item == 1:
                    print("Great choice, I hated that option anyway!")
                    del food_list[delete_item]
                    show_food_option_nums()
                else:
                    print("""
    ARE YOU HAPPY NOW GRUMPY?!
    """)
                    del food_list[delete_item]
                    show_food_option_nums()
                break
            
            else:
                print("You've put the wrong thing in dumbas, try again")

        if (menu == '2'):
            backend()
            break
                