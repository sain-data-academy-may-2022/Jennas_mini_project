import random
import csv
from colorama import Fore, Style
from Colour import Colour_red
from courier_system import Courier_list
from orders import show_order_list, orders1
from food_csv import open_a_csv


with open ('food.csv', 'r') as file:
    read = csv.DictReader(file)
    food_list = list(read)

Index = [sub['Index'] for sub in food_list]
Food_Name = [sub['Food Name'] for sub in food_list]
Description = [sub['Description'] for sub in food_list]
Price = [sub['Price'] for sub in food_list]


def show_food_options():
    open_a_csv()
       

#Ask george on Food name
def add_order_george():
    my_order = int(input("""
I wanna a order a?"""))
    print(f"""
FINALLY, you've chosen a {Food_Name[my_order]}, we now need some details from you? 

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