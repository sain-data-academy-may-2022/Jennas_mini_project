import csv

#at top - to always have access to CSV and food list 
with open ('food.csv', 'r') as file:
        read = csv.DictReader(file)
        food_list = list(read)

      

def write_a_csv():
    headers = ['Index', 'Food Name', 'Description', 'Price']

    with open ('food.csv', 'w') as file:
        write = csv.DictWriter(file, fieldnames= headers) 
        write.writeheader() 
        write.writerows(food_list)

def open_a_csv():
    with open ('food.csv', 'r') as file:
        read = csv.DictReader(file)
        food_list = list(read)
#individual list for each heading to alow access for programme 
        Index = [sub['Index'] for sub in food_list]
        Food_Name = [sub['Food Name'] for sub in food_list]
        Description = [sub['Description'] for sub in food_list]
        Price = [sub['Price'] for sub in food_list]
#for loop - presentation for user - the zip function allows to iterate through multipule lists 
        for i, n, d, p, in zip(Index, Food_Name, Description, Price):
            print(i, n, d, p)

def add_an_item_to_csv():
#adding a new product 
    open_a_csv() 
    custom = input("""
Alright princess, What special dish can your slave make for you?""")
    describe = input (
    """
Any particular type your highness?""")
    Index = [sub['Index'] for sub in food_list] #call index
    Food_Name = [sub['Food Name'] for sub in food_list] #name for user 
    new_index = int(Index[-1]) +1
    add_food_name = [int (new_index), custom, describe, '£1000']
    Food_Name.append(custom)
    with open ('food.csv', 'a', newline= '') as additem:
        new_line = csv.writer(additem)
        new_line.writerow(add_food_name)
    open_a_csv()
    

def update_csv():
    #update product customer facing 
    index_pick = int(input("""
Alright Boss, what do you want to change?
    """))
    value_pick = input( "What do you want to change, Food Name or Description?")
    update = input("to?") 
    food_list[int(index_pick)][value_pick] = update
    write_a_csv()
    open_a_csv()
    


def delete_csv():
    delete_item= int(input(("""
Alright miserable, what do you want to delete?""")))
    if delete_item == 1:
        print("Great choice, I hated that option anyway!")
        del food_list[1]
        write_a_csv()
        open_a_csv()
    else:
        print("""
ARE YOU HAPPY NOW GRUMPY?!
    """)
        del food_list[delete_item]
        write_a_csv()
        open_a_csv()


# print(food_list)
# open_a_csv()



