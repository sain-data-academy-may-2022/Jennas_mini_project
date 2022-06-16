from old.csv_func import open_a_csv, print_csv, save_to_csv
from old.list_func import print_nice_order_list, add_to_a_list



def test_open_csv():
    
    #ASSEMBLE
    my_list = [{'Name': 'Jenna', 'Age': '100'}]
    expected= my_list
    #ACT
    actual = open_a_csv('testcs', 'my_list')
    #ASSERT
    assert expected == actual


test_open_csv()


def test_save_to_csv():
    #ASSEMBLE
    csv_name = 'testcs'
    headers = ['Name', 'Age']
    my_list = [{'Name': 'Jenna', 'Age': '100'}]
    expected= my_list
    #ACT
    actual = save_to_csv(csv_name, headers, my_list)
    #ASSERT
    assert expected == actual

test_save_to_csv()

def test_add_to_a_list():
    #ASSEMBLE    
    my_list = ['Jenna', '123']
    new_item = 'blue'

    expected = ['Jenna', '123', 'blue']
    # ACT
    actual = add_to_a_list(my_list, new_item)
    # ASSERT
    assert expected == actual

test_add_to_a_list()

# def failed_test_add_to_a_list():
#     #ASSEMBLE    
#     my_list = ['Jenna', '123', 'green']
#     new_item = 'blue'

#     expected = ['Jenna', '123', 'blue']
#     # ACT
#     actual = add_to_a_list(my_list, new_item)
#     # ASSERT
#     assert expected == actual

# failed_test_add_to_a_list()


def test_print_nice_order_list():
    # ASSEMBLE
    my_dict = [{'order_id' : '1' ,'customer_name': 'Jenna','customer_address' : 'Thorpe', 'customer_phone' : '123' ,'status' : 'PREPARING','food' : 'cake','courier' : 'Just-Late'}, {'order_id' : '1' ,'customer_name': 'Tom','customer_address' : 'Thorpe', 'customer_phone' : '456' ,'status' : 'PREPARING','food' : 'steak','courier' : 'Deliver-Rude'}]
    expected = print("""1 Jenna Thorpe 123 PREPARING cake Just-Late
1 Tom Thorpe 456 PREPARING steak Deliver-Rude""")
#     # ACT
    actual = print_nice_order_list(my_dict)
    # ASSERT
    assert expected == actual


test_print_nice_order_list()



# def test_print_csv():
#     my_list = [{'Name': 'Tom', 'Age': '21 '}]

#     expected= print(my_list)
    
#     actual = print_csv('testcs', 'New_list')

#     assert expected == actual

# test_print_csv()


# def test_print_a_list():
#     my_list = ['tom', '31']

#     expected = print(my_list)

#     actual =  print_a_list(my_list)
    
#     assert expected == actual

# test_print_a_list()




# def test_update_to_a_list():
#     my_list = [{'Name' : 'Tom', 'Age' : '31'}]
#     pick_item = 0
#     pick_key = 'Age'
#     update = 32

#     expected = [{'Name': 'Tom', 'Age': 32}]

#     actual = update_to_a_list(my_list, pick_item, pick_key, update)

#     assert expected == actual


# test_add_to_a_list()

# def test_delete_from_list():
#     # assemble
#     my_list = [{'Name' : 'Tom', 'Age' : '31'}, {'Name' : 'Jenna', 'Age' : '32'}]
    
#     delete_item = 1
    
#     expected = [{'Name': 'Tom', 'Age': '31'}]
#     # act
#     actual = delete_item_list(my_list, delete_item)
   
# #    assert
#     assert expected == actual

# test_delete_from_list()
