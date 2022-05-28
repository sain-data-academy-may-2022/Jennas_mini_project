import csv
from courier_system import Courier_list
from orders import orders1, show_order_list
import random
from Colour import Colour_red


with open("Food.csv", "r") as f:
        csv_reader = csv.DictReader(f)
        food_list = list(csv_reader)

id = [ sub['ID'] for sub in food_list ]
name = [ sub['Name'] for sub in food_list ]
description = [sub['Description'] for sub in food_list ]
price = [sub['Price'] for sub in food_list ]





def show_food_options():
    id = [ sub['ID'] for sub in food_list ]
    name = [ sub['Name'] for sub in food_list ]
    description = [sub['Description'] for sub in food_list ]
    price = [sub['Price'] for sub in food_list ]
    for i,n,d,p in zip(id, name, description, price):
        print(i, n, d, p)

    
       

def add_order_george():
    show_food_options()
    my_order = int(input("""
    I wanna a order a?"""))


    print(f"""
    FINALLY, you've chosen a {name[my_order]}, we now need some details from you?
    
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
    orders_george["courier"] = random.choice(Courier_list) #RANDOM CHOICE OF COURIER
    orders1.append(orders_george)
    show_order_list()
    
    
    Colour_red("""

    Okay you can start staring out of your window for the driver, if you need to change anything it will cost you.""")