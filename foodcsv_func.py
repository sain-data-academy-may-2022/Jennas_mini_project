import csv
from csv import writer


with open("food.csv", "r") as f:
        csv_reader = csv.DictReader(f)
        food_list = list(csv_reader)



def show_csv():
    with open("Food.csv", "r") as f:
                csv_reader = csv.DictReader(f)
                food_list = list(csv_reader)
                id = [ sub['ID'] for sub in food_list ]
                name = [ sub['Name'] for sub in food_list ]
                for i,n, in zip(id, name):
                        print(i, n,)




#check how to ensure user puts correct thing in 
def add_item():
    with open("Food.csv", "r") as f:
        csv_reader = csv.DictReader(f)
        food_list = list(csv_reader)

    id = [ sub['ID'] for sub in food_list ]
    custom = input("""
Alright princess, What special dish can your slave make for you?""")
    describe = input (
    """
Any particular type your highness?""")
    newid = int(id[-1]) + 1
    add_food =[int(newid), custom, describe, '£1000 (only fair as you are being hard work)']
    with open('food.csv', 'a', newline='') as f: 
        new_line = writer(f)
        new_line.writerow(add_food)  
#look for forced entries i.e drop down look Conn0r
def update_item():
    id_input = int(input("""
    
Alright Boss, what do you want to change?
                            """))
    test = food_list[id_input]
    print(test)
    value = input('What bit do you want to change? ID,Name,Description or Price?')
    change = input('What do you want to change it to?')
    food_list[id_input][value] = change
    titles = ['ID','Name', 'Description', 'Price']
    with open('food.csv', 'w') as csvfile: 
        writer = csv.DictWriter(csvfile, fieldnames = titles)
        writer.writeheader()
        writer.writerows(food_list)

#any other way to write to a specific row within a CSV?
def delete_item():
    id_input = int(input("""
Alright miserable, what do you want to delete?"""))
    if id_input == 1:
        print("Great choice, I hated that option anyway!")
        del food_list[id_input]
        titles = ['ID','Name', 'Description', 'Price']
        with open('food.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = titles)
            writer.writeheader()
            writer.writerows(food_list)
    else:
        print("""
ARE YOU HAPPY NOW GRUMPY?!
    """)
        del food_list[id_input]
        titles = ['ID','Name', 'Description', 'Price']
        with open('food.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames = titles)
            writer.writeheader()
            writer.writerows(food_list)

