cursor.execute(f"""
    SELECT Name

    FROM food

    WHERE product_id = {select_food_choice};""")