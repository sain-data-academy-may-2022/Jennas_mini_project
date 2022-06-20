from colorama import Fore, Back, Style


def Colour_red (text): 
    print(Fore.RED + text)
    print(Style.RESET_ALL)
    return text
    

def print_menu(text: str):
    print(text)
    

def get_input(input_text):
    return input(input_text)


def get_input_int(input_text):
     return int(input(input_text))


food_menu = ("""
Food Menu
        (0) Imma head out.
        (1) See the menu!!!!
        (2) I'm a princess make something special?
        (3) Close, but you want to mix it up a litte?
        (4) Get rid of that!""")

couriers_menu = ("""
Couriers Menu  
        (0) Exit
        (1) Show current couriers names
        (2) Add Courier
        (3) Update a couriers details. 
        (4) Delete a courier.""")

orders_menu = ("""
Orders Menu  
        (0) Exit
        (1) Show current orders?
        (2) Add an order?
        (3) Update a order details? 
        (4) Search by status or courier?
        (5) Stock Check
        (6) Delete an order?""")

customer_menu = ("""
Customer Menu  
        (0) Exit
        (1) Show current customers 
        (2) Add customers
        (3) Update a customers details. 
        (4) Delete a customer.""")

