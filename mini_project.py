import random
from courier_system import Courier_list, Courier_list_fun 
from logins import logins_list_fun
from Colour import prPurple
from Colour import Colour_red
from colorama import Fore, Back, Style
from password import password 
from orders import show_order_list, order_system_fun , orders1


# def clear_screen()
#     # It is for MacOS and Linux(here, os.name is 'posix')
#     if os.name == 'posix':
#         _ = os.system('clear')
#     else:
#         # It is for Windows platfrom
#         _ = os.system('cls')


product = {
    '1' : '(0) Imma head out ',
    '1' : '(1) See the menu!!!!',
    '2' : "(2) I'm a princess make something special?",
    '3' : '(3) Close, but you want to mix it up a litte?',
    '4' : '(4) Get rid of that',
}

food_order ={
   "(0)" : """Chocolate McChocolate Cake: Cake that is chocolate, what more do you need to know""",
   "(1)" : "Salad: A boring choice for a boring person",
   "(2)" : "Hot Chocolate: With Coconut milk to bring that warm chocolately cozyness",
   "(3)" : "Costa'lot Special: Two slices of toast with jam, but we'll charge the cost of a whole loaf""",
   "(4)" : """Vegan Pepperoni Pizza : With lots of meat and chesee from animals, just what you Vegan's want right?"""
}

food_list = ['Chocolate McChocolate Cake','Salad','Hot Chocolate', "Costa'lot Special", "Vegan Pizza"]

#main menu clear screen? 

def show_food_options():
    for key, value in food_order.items():
        print(Fore.RED + key,value)
        print(Style.RESET_ALL)

def show_food_option_nums(): 
      for index,name, in enumerate(food_list):
          print(index,name,)

def add_order_george():
    show_food_options()
    my_order = int(input("""
    I wanna a order a?"""))


    print(f"""
    FINALLY, you've chosen a {food_list[my_order]}, we now need some details from you?
    
    """)
    order_name = input("what's your name mate?")
    order_address = input("where do you live then?")
    order_number = input("Digits?")
    orders_george = {} 
    orders_george["customer_name"] = (order_name)
    orders_george["customer_address"] =(order_address)
    orders_george["customer_phone"] = (order_number)
    orders_george["status"] = ('PREPARING')
    orders_george["food"]= (food_list[my_order])
    orders_george["courier"] = random.choice(Courier_list)
    orders1.append(orders_george)
    show_order_list()
    
    Colour_red("""

    Okay you can start staring out of your window for the driver, if you need to change anything it will cost you.""")
          
    
def backend():
    
    password()
    managers_menu = input ("""
    
You're the best! What do you want to do with these numptys orders? 
(0) Go to the order system
(1) Go to the courier system
(2) Go to the login system
    
    """
    )
    if (managers_menu == '0'):
        order_system_fun()
            
    elif (managers_menu == '1'):
        Courier_list_fun()

    elif (managers_menu== '2'):
        logins_list_fun()

       
#AND WE"RE DONE WITH THE FUNCTIONS!! Now time for the main event "The actual code"

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
            
