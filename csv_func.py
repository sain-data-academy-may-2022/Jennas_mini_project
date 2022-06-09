import csv
import random
from list_func import print_nice_order_list

 # Tested in test.py   

def open_a_csv(csv_name, list_name):
    with open(f'{csv_name}.csv', 'r') as file:
        read = csv.DictReader(file)
        list_name = list(read)
    return list_name

 # Tested in test.py   


def save_to_csv(csv_name: str, headers: list, list_name : list):
    with open (f'{csv_name}.csv', 'w') as file:
        write = csv.DictWriter(file, fieldnames= headers) 
        write.writeheader() 
        write.writerows(list_name)
    return list_name


def print_csv(csv_name , list_name):
    list_name = open_a_csv(csv_name , list_name)
    print(list_name)



# Food CSV

def print_food_csv():
    food_list = open_a_csv('new_food', 'food_list')
    Index = [sub['Index'] for sub in food_list]
    Food_Name = [sub['Food Name'] for sub in food_list]
    Description = [sub['Description'] for sub in food_list]
    Price = [sub['Price'] for sub in food_list]
    for i, n, d, p, in zip(Index, Food_Name, Description, Price):
        print(i, n, d, p)

def print_id_name(food_list):
    Index = [sub['Index'] for sub in food_list]
    Food_Name = [sub['Food Name'] for sub in food_list]
    Price = [sub['Price'] for sub in food_list]
    for i, n, p in zip(Index, Food_Name, Price):
        print(i, n, p)


# ORDER CSV

def add_to_order_csv(order_list, food_list, courier_list):
    order_id = [sub['order_id']for sub in order_list]
    last_id = int(order_id[-1])
    add_order_id = int(last_id + 1)
    add_c_name = input('Whats your name?')
    add_c_address = input('Whats your address?')
    add_c_phone = input('Whats your number?')
    print(food_list)
    which_food = int(input('Which food?'))
    add_food_choice = food_list[which_food]
    add_courier = random.choice(courier_list)
    new_order = {'order_id' : add_order_id, 'customer_name' : add_c_name, 'customer_address' : add_c_address, 'customer_phone' : add_c_phone, 'status': 'Preparing', 'food' : add_food_choice, 'courier' : add_courier}
    order_list.append(new_order)
    print_nice_order_list(order_list)
    

def update_order_status_csv(order_list):
    print_nice_order_list(order_list)
    what_status = int(input ("What status do you want to update?"))
    status_change = input("to?")
    order_list[what_status]['status'] = status_change
    print_nice_order_list(order_list)

def delete_order_from_csv(order_list):
    print_nice_order_list(order_list)
    delete_order = int(input("What order do you want to delete?"))
    del order_list[delete_order]
    print_nice_order_list(order_list)




