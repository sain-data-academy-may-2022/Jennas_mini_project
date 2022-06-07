import json
import csv

from courier_system import Courier_list_fun, courier_list


with open('Orders.json', "r") as file:
    orders1 = json.load(file)

def show_order_list():
    print("Order List:")
    with open ('Orders.json', 'w') as file:
        json.dump(orders1, file, indent=4) 
    for index,order in enumerate(orders1):
        print(index,order)

    headers = ['customer_name','customer_address','customer_phone','status','food','courier']

    with open ('orders.csv', 'w') as file:
        write = csv.DictWriter(file, fieldnames= headers) 
        write.writeheader() 
        write.writerows(orders1)

    
def status_courier_search():
    with open ('orders.csv', 'r') as file:
        read = csv.DictReader(file)
        order_list = list(read)
    status_or_courier = input("Do you want to see orders by Status or Courier?")
    if status_or_courier == 'Status':
        status_pick = input("And what Status orders do you want to see? PREPARING or DELIVERED?")
        for key in order_list:
            if key['status'] == f"{status_pick}":
                print(key)
    if status_or_courier == 'Courier':
        print(courier_list)
        courier_pick = input("What courier are you interested in, just pick the first letter?")
        for key in order_list:
            if key['courier'][10] == f"{courier_pick}":
                print(key)

def order_system_fun():
    while(True):
        orders_options = input("""Orders Menu  

        (0) Exit
        (1) Show current orders? 
        (2) Update an order status? 
        (3) Update a order details? 
        (4) Delete an order?""")
        

        if (orders_options == '0'): 
            print ("""
            Laters""") 
            break

    #show current orders 
        if (orders_options == '1'): 
            show_order_list()
            status_courier_search()
            order_system_fun()
            break
    
    #update an order status 
        if (orders_options == '2'): 
            show_order_list()
            status_update = int(input('which order status do you want to update?'))
            status_change = input('What do you want to change it to?')
            orders1[status_update]["status"] = status_change
            show_order_list()
            order_system_fun()
            break

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
            break
            
            
    #delete an order 
        if (orders_options == '4'):  
            show_order_list()
            delete_order= int(input('Alright, but you aint getting your money back! What order is it?'))
            del orders1[delete_order]
            show_order_list()
            order_system_fun()
            break
            
            print('Thanks for the free cash LOSER!')

        else:
            print("You obviously don't want to change it do you!")







