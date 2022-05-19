from operator import add


product = {
    '0' : '0. Imma head out ',
    '1' : '1. See the menu!!!!',
    '2' : "2. I'm a princess make something special?",
    '3' : '3. Close, but you want to mix it up a litte?',
    '4' : '4. Get rid of that',
    '5' : '5. Access the order system, only if you have placed one though!'
}

# food_order = {
#    "Chocolate McChocolate Cake" : "Cake that is chocolate, what more do you need to know",
#    "Salad:" : "A boring choice for a boring person",
#    "Hot Chocolate" : "With Coconut milk to bring that warm chocolately cozyness",
#    "Costa'lot Special" : "Basically just two slices of toast with jam and no butter, but we've called it special so will charge the cost of a whole loaf"

food_order ={
   "0" : "Chocolate McChocolate Cake: Cake that is chocolate, what more do you need to know",
   "1" : "Salad: A boring choice for a boring person",
   "2" : "Hot Chocolate: With Coconut milk to bring that warm chocolately cozyness",
   "3" : "Costa'lot Special: Basically just two slices of toast with jam and no butter, but we've called it special so will charge the cost of a whole loaf"
}

food_list = ['Chocolate McChocolate Cake','Salad','Hot Chocolate', "Costa'lot Special"]

order1 = {
    "customer_name" : "Jenna",
    "customer_address" :"Thorpe" ,
    "customer_phone" : "07999999999",
    "status" : "PREPARING",
}

order2 = {
    "customer_name" : "",
    "customer_address" :"" ,
    "customer_phone" : "",
    "status" : "PREPARING",
}

orders = [order1,order2]

def show_food_options():
    for key, value in food_order.items():
        print(key,value)

def show_food_option_nums(): 
      for index,name, in enumerate(food_list):
          print(index,name,)

def show_order_list():
      for index,order in enumerate(orders):
          print(index,order)


def add_order_george():
    show_food_options
    my_order = int(input('I wanna a order a?'))
    print(f"Thank you for placing your order for a {food_list[my_order]}, we now need some details from you?")
    order_name = input("what's your name mate?")
    order_address = input("where do you live then?")
    order_number = input("Digits?")
    orders_george = {}
    orders_george["customer_name"] = (order_name)
    orders_george["customer_address"] =(order_address)
    orders_george["customer_phone"] = (order_number)
    orders_george["Status"] = ('PREPARING')
    print(orders_george)  
    orders.append(orders_george)


def order_finished():
    q_order_finish = input("Press '1' to exit and start staring out of your window for the driver. Press '2' to go to the order system")
    if (q_order_finish == '2'):
        order_system_fun()
    if (q_order_finish == '1'):
        print('Okay he is on his way ')
            
    
def order_system_fun():
    orders_options = input("What do you want to do then? (0). Show current orders? (1). Update an order status? (2). Update a order details? (3). Delete an order?")
    if (orders_options == '0'):
        show_order_list()
        order_system_fun()
    if (orders_options == '1'):
        show_order_list()
        status_update = int(input('which order status do you want to update?'))
        status_change = input('What do you want to change it to?')
        orders[status_update]["status"] = status_change
        show_order_list()
    if (orders_options == '2'):
        show_order_list()
        status_update = int(input('which order details do you want to update?'))
        print('Only update what you got wrong! Otherwise press enter so you dont mess up more!')
        order_name1 = input("what's your name mate?")
        if order_name1 == "":
                pass
        order_address1 = input("where do you live then?")
        if order_address1 == "":
                order_address1 = orders[status_update]["customer_address"] = order_address1
        order_number1 = input("Digits?")
        if order_number1 == "":
                pass
        orders[status_update]["customer_name"] = order_name1
        orders[status_update]["customer_address"] = order_address1
        orders[status_update]["customer_number"] = order_number1
        show_order_list()
        
           

    if (orders_options == '3'):
        show_order_list()
        delete_order= int(input('Alright, but you aint getting your money back! What order is it?'))
        del orders[delete_order]
        show_order_list()
        print('Thanks for the free cash LOSER!')
       
#The actual code

while(True):
    print("This is the Costa'lot app! To exit app choose 0, to see our options choose 1:")
    menu = input()
    if (menu == '0') or (menu == 'no'):
        print("FINE GO! Our Chocolate Cake is AMAZING, I'll get your money next time!'") 
        break

    elif (menu == '1') or (menu == 'yes'):
        for key, value in product.items() :
                print(value)
        choice =  (input('Hurry up and pick something would you?'))
    
    if (choice == '0'):
        print("FINE GO! Our Chocolate Cake is AMAZING, I'll get your money next time!'") 
        break
           
    elif (choice == '1'):
        show_food_options()
        add_order_george()
        order_finished()
        break

    elif (choice == '2'):
        custom = input('Alright princess, What special dish can your slave make for you?')
        describe = input ('Any particular type your highness?')
        food_list.append(custom)
        custom_1 = (f"{custom}: {describe}")
        food_order[4] = custom_1 
        show_food_options()
        add_order_george()
        order_finished()
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
        order_finished()
        break
        

    elif (choice == '4'):
        print('Alright miserable, what do you want to delete?')
        show_food_options()
        delete_item= input()
        del food_order[delete_item]
        show_food_options()
        print('ARE YOU HAPPY NOW GRUMPY?!')
        break

    elif (choice == '5'): 
        order_system_fun()
        break
    