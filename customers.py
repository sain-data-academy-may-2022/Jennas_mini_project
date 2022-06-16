from colorama import Cursor
import database_func
import menus


connection = database_func.get_connection()
cursor = connection.cursor()
add_c_name = menus.get_input('Whats your name?')
add_c_address = menus.get_input('Whats your address?')
add_c_phone = menus.get_input_int('Whats your number?')
sql = ("INSERT INTO customers (customer_name, customer_address, customer_phone) VALUES (%s, %s, %s)")
val = (f"{add_c_name}", f"{add_c_address}", add_c_phone)
cursor.execute(sql,val)
connection.commit()
cursor.close()
connection.close()


