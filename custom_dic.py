#Create a custom dic within the base code
# print(f"Thank you for placing your order for a we now need some details from you")
# order_name = input("what's your name mate?")
# order_address = input("where do you live then?")
# order_number = input("Digits?")
# order_name = {
#     "customer_name" : order_name,
#     "customer_address" : order_address,
#     "customer_phone" : order_number,
#     "customer_status" : "PREPARING"
# }
# order_list= [order_name]
# print(order_list)
  

# print('Only update what you got wrong! Otherwise press enter so you dont mess up more!')
# order_name1 = input("what's your name mate?")
# if order_name1 == "":
#     order_name1 = order_name["customer_name"]
# order_address1 = input("where do you live then?")
# if order_address1 == "":
#     order_address1 = order_name["customer_address"]
# order_number1 = input("Digits?")
# if order_number1 == "":
#     order_number1 = order_name["customer_phone"]
# order_name["customer_name"] = (order_name1)
# order_name["customer_address"] =(order_address1)
# order_name["customer_phone"] = (order_number1)

# print(order_list)

#custom_dic as a fucntion so can be repeatable

def add_order():
    print(f"Thank you for placing your order for a we now need some details from you")
    order_name = input("what's your name mate?")
    order_address = input("where do you live then?")
    order_number = input("Digits?")
    order_name = {
        "customer_name" : order_name,
        "customer_address" : order_address,
        "customer_phone" : order_number,
        "customer_status" : "PREPARING"
    }
    order_list= [order_name]
    print(order_list)
  

print('Only update what you got wrong! Otherwise press enter so you dont mess up more!')
order_name1 = input("what's your name mate?")
if order_name1 == "":
    order_name1 = order_name["customer_name"]
order_address1 = input("where do you live then?")
if order_address1 == "":
    order_address1 = order_name["customer_address"]
order_number1 = input("Digits?")
if order_number1 == "":
    order_number1 = order_name["customer_phone"]
order_name["customer_name"] = (order_name1)
order_name["customer_address"] =(order_address1)
order_name["customer_phone"] = (order_number1)

print(order_list)

