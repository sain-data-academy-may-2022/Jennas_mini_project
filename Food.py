import random
from colorama import Fore, Style
from Colour import Colour_red
from courier_system import Courier_list
from orders import show_order_list, orders1


Food_dict =[
    {'ID' : 0,
    'Name': 'Chocolate McChocolate Cake: ',
    'Description': 'Cake that is chocolate, what more do you need to know',
    'Price': '£20'},

    {'ID' : 1,
    'Name': 'Salad: ',
    'Description': 'A boring choice for a boring person',
    'Price': '£666'},

    {'ID' : 2,
    'Name': 'Hot Chocolate:',
    'Description': 'With Coconut milk to bring that warm chocolately cozyness',
    'Price': '£10'
    },

    {'ID' : 3,
    'Name': "Costa'lot Special: ",
    'Description': "Two slices of toast with jam, but we'll charge the cost of a whole loaf",
    'Price': '£12'
    },

    {'ID' : 4,
    'Name': "Vegan Pepperoni Pizza: ",
    'Description': "With lots of meat and chesee from animals, just what you Vegan's want right?",
    'Price': '£23'}
    ]



food_list = ['Chocolate McChocolate Cake','Salad','Hot Chocolate', "Costa'lot Special", "Vegan Pizza"]
    

def show_food_options():
    for key, value in Food_dict.items():
        print(key,value)
       

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
    orders_george["courier"] = random.choice(Courier_list) #RANDOM CHOICE OF COURIER
    orders1.append(orders_george)
    show_order_list()
    
    Colour_red("""

    Okay you can start staring out of your window for the driver, if you need to change anything it will cost you.""")