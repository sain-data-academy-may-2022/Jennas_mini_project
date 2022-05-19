product = {
    '0' : '0. Imma head out ',
    '1' : '1. See the menu!!!!',
    '2' : "2. I'm a princess make something special?",
    '3' : '3. Close, but you want to mix it up a litte?',
    '4' : '4. Get rid of that',
    '5' : '5. Access the order system, only if you have placed one though!'
}

food_order = {
   "1" : "Chocolate McChocolate Cake``: Cake that is chocolate, what more do you need to know",
   "2" : "Salad: A boring choice for a boring person",
   "3" : "Hot Chocolate: With Coconut milk to bring that warm chocolately cozyness",
   "4" : "Costa'lot Special: Basically just two slices of toast with jam and no butter, but we've called it special so will charge the cost of a whole loaf"
}

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

def show_food_options(): 
       for key, value in food_order.items():
                print(key, value)

def show_order_list():
       print("Order '1' ")
       for key, value in order1.items():
                print(key, value)

def show_order_list2():
       print("Order '2'")
       for key, value in order2.items():
                print(key, value)


def add_order():
    my_order = (input('I wanna a order a?'))
    print(f"Thank you for placing your order for a {food_order [my_order]}, we now need some details from you?")
    order_name = input("what's your name mate?")
    order_address = input("where do you live then?")
    order_number = input("Digits?")
    order1["customer_name"] = (order_name)
    order1["customer_address"] =(order_address)
    order1["customer_phone"] = (order_number)
    show_order_list ()

def new_add_order():
    my_order = int(input('I wanna a order a?'))
    print(f"Thank you for placing your order for a {food_order [my_order]}, we now need some details from you")
    order_name = input("what's your name mate?")
    order_address = input("where do you live then?")
    order_number = input("Digits?")
    order2["customer_name"] = (order_name)
    order2["customer_address"] =(order_address)
    order2["customer_phone"] = (order_number)
    show_order_list2()  
    
    

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
        show_order_list2()
        order_system_fun()
    if (orders_options == '1'):
        show_order_list() 
        show_order_list2()
        status_update = (input('which order status do you want to update?'))
        if (status_update == '1'):
            status_change = input('What do you want to change it to?')
            order1["status"] = (status_change)
            #order1["status"] = "Delivered"
            show_order_list()
        elif (status_update == '2'):
            status_change = input('What do you want to change it to?')
            order2["status"] = (status_change)
            show_order_list2()
    if (orders_options == '2'):
        show_order_list() 
        show_order_list2()
        status_update = (input('which order details do you want to update?'))
        if (status_update == '1'):
            print('Only update what you got wrong! Otherwise press enter so you dont mess up more!')
            order_name1 = input("what's your name mate?")
            if order_name1 == "":
                order_name1 = order1["customer_name"]
            order_address1 = input("where do you live then?")
            if order_address1 == "":
                order_address1 = order1["customer_address"]
            order_number1 = input("Digits?")
            if order_number1 == "":
                order_number1 = order1["customer_phone"]
            order1["customer_name"] = (order_name1)
            order1["customer_address"] =(order_address1)
            order1["customer_phone"] = (order_number1)
            show_order_list()
        elif (status_update == '2'):
            print('Only update what you got wrong! Otherwise press enter so you dont mess more up!')
            order_name1 = input("what's your name mate?")
            if order_name1 == "":
                order_name1 = order2["customer_name"]
            order_address1 = input("where do you live then?")
            if order_address1 == "":
                order_address1 = order2["customer_address"]
            order_number1 = input("Digits?")
            if order_number1 == "":
                order_number1 = order2["customer_phone"]
            order2["customer_name"] = (order_name1)
            order2["customer_address"] =(order_address1)
            order2["customer_phone"] = (order_number1)
            show_order_list2()
           

    if (orders_options == '3'):
        show_order_list() 
        show_order_list2()
        delete_order= input('Alright, but you aint getting your money back! What order is it?')
        if delete_order == '1':
            dict.clear (order1)
            show_order_list() 
            show_order_list2()
            print('Thanks for the free cash LOSER!')
        if delete_order == '2':
            dict.clear (order2)
            show_order_list() 
            show_order_list2()
            print('Thanks for the free cash LOSER!')
       
#The actual code

while(True):
    print("This is the Costa'lot app! To exit app choose 0, to see our options choose 1:")
    menu = input()
    if (menu == '0') or (menu == 'no'):
        print("FINE GO!!!!!! I'll get your money next time!'") 
        break

    elif (menu == '1') or (menu == 'yes'):
        for key, value in product.items() :
                print(value)
        choice =  (input('Hurry up and pick something would you?'))
    
    if (choice == '0'):
        print('Sending you back to the start.')
           
    elif (choice == '1'):
        show_food_options()
        new_add_order()
        order_finished()
        break

    elif (choice == '2'):
        custom = input('Alright princess, What special dish can your slave make for you?')
        describe = input ('Any particular type your highness?')
        custom_1 = (f"{custom}: {describe}")
        food_order [5] =  (custom_1)
        show_food_options()
        new_add_order()
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
        new_add_order()
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
        

    
        # order_system_fun()

            
            


      




    

    


    