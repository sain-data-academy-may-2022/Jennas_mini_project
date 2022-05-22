import json
import getpass
import os
from turtle import update


from password import password 
# def clear_screen():
#     # It is for MacOS and Linux(here, os.name is 'posix')
#     if os.name == 'posix':
#         _ = os.system('clear')
#     else:
#         # It is for Windows platfrom
#         _ = os.system('cls')


product = {
    '0' : '0. Imma head out ',
    '1' : '1. See the menu!!!!',
    '2' : "2. I'm a princess make something special?",
    '3' : '3. Close, but you want to mix it up a litte?',
    '4' : '4. Get rid of that',
}

food_order ={
   "0" : "Chocolate McChocolate Cake: Cake that is chocolate, what more do you need to know",
   "1" : "Salad: A boring choice for a boring person",
   "2" : "Hot Chocolate: With Coconut milk to bring that warm chocolately cozyness",
   "3" : "Costa'lot Special: Two slices of toast with jam, but we'll charge the cost of a whole loaf"
}

food_list = ['Chocolate McChocolate Cake','Salad','Hot Chocolate', "Costa'lot Special"]

# order1 = {
#     "customer_name" : "Jenna",
#     "customer_address" :"Thorpe" ,
#     "customer_phone" : "07999999999",
#     "status" : "PREPARING",
#     "food" : "Hot Chocolate"
# }

with open('Orders.json', "r") as file:
    orders = json.load(file)

if type(orders) is dict:
    orders = [orders]



def show_food_options():
    for key, value in food_order.items():
        print(key,value)

def show_food_option_nums(): 
      for index,name, in enumerate(food_list):
          print(index,name,)

def show_order_list():
      print("Order List:")
      with open ('Orders.json', 'w') as file:#how to append rather that w
                json.dump(orders, file) 
      for index,order in enumerate(orders):
          print(index,order) 


# #warm up fun 20/3
def add_order_george():
    show_food_options()
    my_order = int(input('I wanna a order a?'))
    print(f"FINALLY, you've chosen a {food_list[my_order]}, we now need some details from you?")
    order_name = input("what's your name mate?")
    order_address = input("where do you live then?")
    order_number = input("Digits?")
    orders_george = {} #create new dictorary 
    orders_george["customer_name"] = (order_name)
    orders_george["customer_address"] =(order_address)
    orders_george["customer_phone"] = (order_number)
    orders_george["status"] = ('PREPARING')
    orders_george["food"]= (food_list[my_order])
    orders.append(orders_george)
    show_order_list()
    print('Okay you can start staring out of your window for the driver, if you need to change anything it will cost you.')
        
     #the big one - task we were set this week        
    
def order_system_fun():
    orders_options = input("""What do you want to do then? 
    0. Exit
    1. Show current orders? 
    2. Update an order status? 
    3. Update a order details? 
    4. Delete an order?""")
    

    if (orders_options == '0'): 
        print ('See you later loser')


    if (orders_options == '1'): #show current orders 
        show_order_list()
        order_system_fun()


    if (orders_options == '2'): #update an order status 
        show_order_list()
        status_update = int(input('which order status do you want to update?'))
        status_change = input('What do you want to change it to?')
        orders[status_update]["status"] = status_change
        show_order_list()
        order_system_fun()


    if (orders_options == '3'): #update order details 
        show_order_list()
        status_update = int(input('which order details do you want to update?'))
        for key, value in orders[status_update].items():
            y_n = input(f"Do you wish to update {key} from {value}? >").upper()
            if y_n == "Y":
                new_value = input(f'Enter new value for {key}. >') 
                orders[status_update]["key"] = new_value
            else:
                continue
        with open ('Orders.json', 'w') as file:#how to append rather that w
            json.dump(orders, file) 

        show_order_list()
        order_system_fun()
        
           

    if (orders_options == '4'): #delete an order 
        show_order_list()
        delete_order= int(input('Alright, but you aint getting your money back! What order is it?'))
        del orders[delete_order]
        show_order_list()
        print('Thanks for the free cash LOSER!')


def backend():
    password()
    managers_menu = input ("""You're the best! What do you want to do with these numptys orders? 
    (0) Go to the order system
    (1) Go to the courier system""")
    if (managers_menu == '0'):
            order_system_fun()
             
    elif (managers_menu == '1'):
        from courier_system import Courier_list_fun
        Courier_list_fun()

       
#AND WE"RE DONE WITH THE FUNCTIONS!! Now time for the main event "The actual code"

while(True):
    print("""This is the Costa'lot app!
    (0) To exit app.
    (1) To see our food options and place an order.
    (2) For the governer only (Do you know the magic word? If not don't even try it!)""")

    menu = input()
    if (menu == '0') or (menu == 'no'):
        print("FINE GO! Our Chocolate Cake is AMAZING, I'll get your money next time!'") 
        break

    if (menu == '1') or (menu == 'yes'):
        for key, value in product.items() :
                print(value)
        choice =  (input('Hurry up and pick something would you?')) 

        if (choice == '1'):
            add_order_george()
            break

        elif (choice == '2'):
            custom = input('Alright princess, What special dish can your slave make for you?')
            describe = input ('Any particular type your highness?')
            food_list.append(custom)
            custom_1 = (f"{custom}: {describe}")
            food_order[4] = custom_1 
            show_food_options()
            add_order_george()
            break
            
                
        elif (choice == '3'):
            print(('Alright Boss, what do you want to change?'))
            show_food_options()
            update_item= input ()
            item_change = input('Just remeber your own ideas cost more, but what is it?')
            item_description = input('In more detail please?!?!')
            item_1 = (f"{item_change}: {item_description}")
            food_order[update_item] = item_1
            show_food_options()
            add_order_george()
            break
            

        elif (choice == '4'):
            print('Alright miserable, what do you want to delete?')
            show_food_options()
            delete_item= input()
            del food_order[delete_item]
            show_food_options()
            print('ARE YOU HAPPY NOW GRUMPY?!')
            break
        
        else:
            print("You've put the wrong thing in dumbas, try again")

    if (menu == '2'):
        backend()
        break
            