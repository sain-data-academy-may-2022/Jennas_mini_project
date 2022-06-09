
def add_to_a_list (my_list : list, new_item):
    my_list.append(new_item)
    return my_list

def print_nice_order_list(order_list):
    order_id = [sub['order_id']for sub in order_list]
    name = [sub['customer_name'] for sub in order_list]
    address = [sub['customer_address'] for sub in order_list]
    phone = [sub['customer_phone'] for sub in order_list]
    status = [sub['status'] for sub in order_list]
    food = [sub['food'] for sub in order_list]
    courier = [sub['courier'] for sub in order_list]
    for oi, n, a, p, s, f, c in zip(order_id, name, address, phone, status, food, courier):
        print(oi, n ,a , p, s, f, c)


# def update_to_a_list(my_list : list, pick_item : int, pick_key : str, update):
#     my_list[pick_item][pick_key] = update
#     return my_list

# def delete_item_list (my_list : list, delete_item : int):
#     del my_list[delete_item]
#     return my_list

# def print_a_list(my_list : list):
#     print(my_list)