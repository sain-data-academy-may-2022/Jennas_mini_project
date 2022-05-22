# Courier_list = ['Deliver-rude', 'Just-stave', 'Uber-steal',]


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
        orders[status_update]["customer_phone"] = order_number1
        show_order_list()
        order_system_fun()
        
           

    if (orders_options == '4'): #delete an order 
        show_order_list()
        delete_order= int(input('Alright, but you aint getting your money back! What order is it?'))
        del orders[delete_order]
        show_order_list()
        print('Thanks for the free cash LOSER!')