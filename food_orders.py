import database_func
from prettytable import PrettyTable
import menus


food_headers = ['product_id', 'food_name', 'description', 'food_price', 'quantity']

connection = database_func.get_connection()
cursor = connection.cursor()
cursor.execute(f'Select * FROM food')
rows = cursor.fetchall()
x = PrettyTable()
x.field_names = food_headers
for row in rows:
    x.add_row(row)
print(x)


add_c_name = menus.get_input('Whats your name?')
add_c_address = menus.get_input('Whats your address?')
add_c_phone = menus.get_input_int('Whats your number?')
sql = ("INSERT INTO customers (customer_name, customer_address, customer_phone) VALUES (%s, %s, %s)")
val = (f"{add_c_name}", f"{add_c_address}", add_c_phone)
cursor.execute(sql,val)
cursor.execute("SELECT customer_id FROM customers WHERE customer_id=(SELECT max(customer_id) FROM customers);")
customer_id = cursor.fetchone()
order1 = int(input("what would you like to order? Please enter the product_id? "))
how_many1 = int(input("And how many? "))
cursor.execute(f"SELECT food_price * {how_many1} as TOTAL FROM food WHERE product_id= {order1};")
price = cursor.fetchall()
sql = ("INSERT INTO food_orders (product_id, quantity, price) VALUES (%s, %s, %s)")
val = (f"{order1}", f"{how_many1}", {price})
cursor.execute(sql,val)
cursor.execute("SELECT order_id FROM food_orders WHERE order_id=(SELECT max(order_id) FROM food_orders);")
order_id = cursor.fetchone()  
sql = ("INSERT INTO customer_orders (customer_id, order_id) VALUES (%s, %s)")
val = ({customer_id}, {order_id})
cursor.execute(sql,val)
connection.commit()
more = input("Do you want to order anything else? y or n")
if more == "y":
    cursor.execute(f'Select * FROM food')
    rows = cursor.fetchall()
    x = PrettyTable()
    x.field_names = food_headers
    for row in rows:
        x.add_row(row)
    print(x)
    order2 = int(input("what would you like to order? Please enter the product_id? "))
    how_many2 = int(input("And how many? "))
    cursor.execute("SELECT order_id FROM food_orders WHERE order_id=(SELECT max(order_id) FROM food_orders);")
    order_id = cursor.fetchone()  
    cursor.execute(f"SELECT food_price * {how_many2} as TOTAL FROM food WHERE product_id= {order2};")
    price = cursor.fetchall()
    sql = ("INSERT INTO food_orders (order_id, product_id, quantity, price) VALUES (%s,%s, %s, %s)")
    val = ({order_id}, {order2}, {how_many2}, {price})
    cursor.execute(sql,val)
    connection.commit()


    

#     more = input("Do you want to order anything else? y or n? ")
# #     if more == "n":
        # cursor.execute(f' SELECT food_name FROM food WHERE product_id = {order1};')
        # food_choice1 = cursor.fetchall()
        # print(f'So you want a product {food_choice1} and you want {how_many1} of them. Your order has been loaded')
        # cursor.execute(f"SELECT food_price * {how_many1} as TOTAL FROM food WHERE product_id= {order1};")
        # price = cursor.fetchall()
        # sql = ("INSERT INTO food_orders (product_id, quantity, price) VALUES (%s, %s, %s)")
        # val = (f"{order1}", f"{how_many1}", {price})
        # cursor.execute(sql,val)
        # connection.commit()
        # break

# #     elif more == "y":
# #         cursor.execute(f' SELECT food_name FROM food WHERE product_id = {order1};')
# #         food_choice1 = cursor.fetchall()
# #         print(f'So you want a product {food_choice1} and you want {how_many1} of them. Your order has been loaded')
# #         cursor.execute(f"SELECT food_price * {how_many1} as TOTAL FROM food WHERE product_id= {order1};")
# #         price = cursor.fetchall()
# #         sql = ("INSERT INTO food_orders (product_id, quantity, price) VALUES (%s, %s, %s)")
# #         val = (f"{order1}", f"{how_many1}", {price})
# #         cursor.execute(sql,val)
# #         connection.commit()
# #         try:
# #             order2 = int(input("what would you like to order? Please enter the product_id? "))
# #         except ValueError:
# #             print("PRODUCT ID")
# #             order2 = int(input("what would you like to order? Please enter the product_id? "))
# #         try:    
# #             how_many2 = int(input("And how many? "))
# #         except ValueError:
# #             print("I need a number mate, come on")
# #             how_many2 = int(input("And how many? "))
# #         cursor.execute(f' SELECT food_name FROM food WHERE product_id = {order1};')
# #         food_choice1 = cursor.fetchall()
# #         cursor.execute(f' SELECT food_name FROM food WHERE product_id = {order2};')
# #         food_choice2 = cursor.fetchall()
# #         more2 = input("Do you want to order anything else? y or n? ")
# #         if more2 == 'n':
# #             print(f"Right. You want {how_many1} x {food_choice1} and {how_many2} x {food_choice2}. Letting loose are we?")
# #             cursor.execute("SELECT order_id FROM food_orders WHERE order_id=(SELECT max(order_id) FROM food_orders);")
# #             order_id = cursor.fetchall()
# #             cursor.execute(f"SELECT food_price * {how_many2} as TOTAL FROM food WHERE product_id= {order2};")
# #             price = cursor.fetchall()
# #             sql = ("INSERT INTO food_orders (order_id,product_id, quantity, price) VALUES (%s, %s, %s, %s)")
# #             val = ({order_id}, f"{order2}", f"{how_many2}", {price})
# #             cursor.execute(sql,val)
# #             connection.commit()
# #             break 
# #         elif more2 == 'y':
# #             try:
# #                 order3 = int(input("what would you like to order? Please enter the product_id? "))
# #             except ValueError:
# #                 print("PRODUCT ID")
# #                 order3 = int(input("what would you like to order? Please enter the product_id? "))
# #             try:    
# #                 how_many3 = int(input("And how many? "))
# #             except ValueError:
# #                 print("I need a number mate, come on")
# #                 how_many3 = int(input("And how many? "))
# #             cursor.execute(f' SELECT food_name FROM food WHERE product_id = {order1};')
# #             food_choice1 = cursor.fetchall()
# #             cursor.execute(f' SELECT food_name FROM food WHERE product_id = {order2};')
# #             food_choice2 = cursor.fetchall()
# #             cursor.execute(f' SELECT food_name FROM food WHERE product_id = {order2};')
# #             food_choice3 = cursor.fetchall()
# #             print (f"Right that's your lot. You want {how_many1} x {food_choice1}, {how_many2} x {food_choice2} and {how_many3} x {food_choice3}. Greedy Pig")
# #             break

# #         else:
# #             print("Are you stupid? Back to the start!")
    
# #     else:
# #         print("Are you stupid? Try again!")




# cursor.execute("SELECT order_id + 1 FROM food_orders WHERE order_id=(SELECT max(order_id) FROM food_orders);")
# order_id = cursor.fetchone()
# cursor.execute(f"SELECT food_price * {2} as TOTAL FROM food WHERE product_id= {1};")
# price = cursor.fetchall()
# sql = ("INSERT INTO food_orders (order_id, product_id, quantity, price) VALUES (%s, %s, %s, %s)")
# val = (f"{order_id}", f"1", f"2", {price})
# # print(val)
# cursor.execute(sql,val)
# connection.commit()





# # connection = database_func.get_connection()
# # cursor.execute("""SELECT SUM(food_price) FROM food
# # WHERE product_id IN ('1','2');
# # """)
# # sum = cursor.fetchall()




# # =
# # sql = ("INSERT INTO food_orders (product_id, quantity, price) VALUES (%s, %s, %s)")
# # val = (f"{order1}", f"{how_many1}", )
# # cursor.execute(sql,val)
# # connection.commit()
# # cursor.close()
# # connection.close(






