from database_func import cursor
# cursor.execute('SET FOREIGN_KEY_CHECKS=0')
# cursor.execute("TRUNCATE TABLE customer_orders;")

cursor.execute(f"""SELECT SUM(quantity) FROM food_orders
WHERE product_id = (1);
""")
amount_of_cake = cursor.fetchall()
total_cake = int(amount_of_cake[0][0])

cursor.execute(f"""SELECT SUM(quantity) FROM food_orders
WHERE product_id = (2);
""")
amount_of_salad = cursor.fetchall()
total_salad = int(amount_of_salad[0][0])

cursor.execute(f"""SELECT SUM(quantity) FROM food_orders
WHERE product_id = (3);
""")
amount_of_hotchoc = cursor.fetchall()
total_hotchoc = int(amount_of_hotchoc[0][0])

cursor.execute(f"""SELECT SUM(quantity) FROM food_orders
WHERE product_id = (4);
""")
amount_of_special = cursor.fetchall()
total_special = int(amount_of_special[0][0])

cursor.execute(f"""SELECT SUM(quantity) FROM food_orders
WHERE product_id = (5);
""")
amount_of_vegan = cursor.fetchall()
total_vegan = int(amount_of_vegan[0][0])


# cursor.execute(f"""SELECT SUM(quantity) FROM food_orders
# WHERE product_id = (8);
# """)
# amount_of_pie = cursor.fetchall()
# total_pie = int(amount_of_pie[0][0])


# cursor.execute("SELECT product_id FROM food WHERE product_id=(SELECT max(product_id) FROM food);")
# last_id = cursor.fetchone()
# last_id1 = int(last_id[0])
# # print(last_id1)

# cursor.execute(f"""SELECT SUM(quantity) FROM food_orders
# WHERE product_id = ({last_id1});
# """)
# amount_of_last = cursor.fetchall()
# total_last = int(amount_of_last[0][0])



total_sales = [total_cake, total_salad, total_hotchoc, total_special, total_vegan]