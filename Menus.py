from password import password
from orders import order_system_fun
from courier_system import Courier_list_fun
from logins import logins_list_fun
from Colour import Colour_red
from Food import add_order_george, food_list, food_order, show_food_options, show_food_option_nums
       
#all menus in the same place 
#start with the opening menu - that you have seen before 

def The_App_I_Think_Maybe():
    while(True):
        Colour_red(""" 
                                    ---- Costa'lot ---- 
                                    

    (0) To exit app.
    (1) To see our food options and place an order.
    (2) For the governer only (Do you know the magic word? If not don't even try it!
    
                                   --------------------""")

        menu = input()
        if (menu == '0'):
            Colour_red("FINE GO! Our Chocolate Cake is AMAZING, I'll get your money next time!'") 
            break

        if (menu == '1'):
            food_menu()

        if menu == '2':
            backend()

        else:
            print("PICK 0 or 1, it's not hard dumbass!")

#Food options - seen before 

def food_menu():

    while(True):
        choice =  (input("""

(0) Imma head out ',
(1) See the menu!!!!',
(2) I'm a princess make something special?",
(3) Close, but you want to mix it up a litte?',
(4) Get rid of that',

Hurry up and pick something would you?
            
            """)) 

        if (choice == '1'):
            add_order_george()
            break

        elif (choice == '2'):
            custom = input("""
Alright princess, What special dish can your slave make for you?""")
            describe = input (
"""
Any particular type your highness?""")
            food_list.append(custom)
            custom_1 = (f"{custom}: {describe}")
            food_order[(f'({5})')] = custom_1 
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

        
# - this is a backend menu - as i feel i have two user groups - this would be for mgrs 
def backend():
    
#as this is for mgr use - password function 

    password()
    
    while(True): 
        managers_menu = input ("""
You're the best! What do you want to do with these numptys orders? 
(0) Go to the order system
(1) Go to the courier system
(2) Go to the login system
    
    """
    )
        if (managers_menu == '0'):
            order_system_fun()
            break
                
        elif (managers_menu == '1'):
            Courier_list_fun()
            break

        elif (managers_menu== '2'):
            logins_list_fun()
            break

        else:
            print("Come on you work here! You should know this stuff!")