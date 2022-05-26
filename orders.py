import json

with open('Orders.json', "r") as file:
    orders1 = json.load(file)

if type(orders1) is dict:
    orders1 = [orders1]

def show_order_list():
      print("Order List:")
      with open ('Orders.json', 'w') as file:
          json.dump(orders1, file, indent=4) 
      for index,order in enumerate(orders1):
          print(index,order) 

def order_system_fun():
    orders_options = input("""Orders Menu  

    (0) Exit
    (1) Show current orders? 
    (2) Update an order status? 
    (3) Update a order details? 
    (4) Delete an order?""")
    

    if (orders_options == '0'): 
        print ("""
        Laters""")

#show current orders 
    if (orders_options == '1'): 
        show_order_list()
        order_system_fun()
 
#update an order status 
    if (orders_options == '2'): 
        show_order_list()
        status_update = int(input('which order status do you want to update?'))
        status_change = input('What do you want to change it to?')
        orders1[status_update]["status"] = status_change
        show_order_list()
        order_system_fun()

 #update order details 
    if (orders_options == '3'): 
        show_order_list()
        status_update = int(input('What idiot wants their order changed then?'))
        for key, value in orders1[status_update].items():
            new_value = input(f'Is it {key}? If by some miracle they have actually got it right just press enter >')
            if new_value == "":
                continue
            else:
                orders1[status_update][key] = new_value
        show_order_list()
        order_system_fun()
        
           
#delete an order 
    if (orders_options == '4'):  
        show_order_list()
        delete_order= int(input('Alright, but you aint getting your money back! What order is it?'))
        del orders1[delete_order]
        show_order_list()
        
        print('Thanks for the free cash LOSER!')