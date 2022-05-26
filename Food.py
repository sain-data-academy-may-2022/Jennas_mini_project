import random
from colorama import Fore, Style
from Colour import Colour_red
from courier_system import Courier_list
from orders import show_order_list, orders1


food_order ={
   "(0)" : """Chocolate McChocolate Cake: Cake that is chocolate, what more do you need to know""",
   "(1)" : "Salad: A boring choice for a boring person",
   "(2)" : "Hot Chocolate: With Coconut milk to bring that warm chocolately cozyness",
   "(3)" : "Costa'lot Special: Two slices of toast with jam, but we'll charge the cost of a whole loaf""",
   "(4)" : """Vegan Pepperoni Pizza : With lots of meat and chesee from animals, just what you Vegan's want right?"""
}

food_list = ['Chocolate McChocolate Cake','Salad','Hot Chocolate', "Costa'lot Special", "Vegan Pizza"]
    

def show_food_options():
    for key, value in food_order.items():
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
    orders_george["courier"] = random.choice(Courier_list)
    orders1.append(orders_george)
    show_order_list()
    
    Colour_red("""

    Okay you can start staring out of your window for the driver, if you need to change anything it will cost you.""")