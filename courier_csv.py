import csv


with open ('courier.csv', 'r') as file:
        read = csv.DictReader(file)
        courier_list = list(read)

        Name_list= [sub['Name'] for sub in courier_list]
        Phone_list = [sub['Phone'] for sub in courier_list]


def write_a_csv():
    titles = ['Name', 'Phone']

    with open ('courier.csv', 'w') as file:
        write = csv.DictWriter(file, fieldnames= titles) 
        write.writeheader() 
        write.writerows(courier_list)

def open_a_csv():
    with open ('courier.csv', 'r') as file:
        read = csv.DictReader(file)
        courier_list = list(read)

        Name_list = [sub['Name'] for sub in courier_list]
        Phone_list = [sub['Phone'] for sub in courier_list]
        for n, p, in enumerate(zip(Name_list, Phone_list)):
            print(n, p)

def add_an_item_to_csv():

    open_a_csv() 
    custom = input("""
What's the name? They best not be some idiot on a bike!""")
    custom_number = input("""
And their number?""")
    add_courier_name = [custom, custom_number]
    Name_list.append(custom)
    Phone_list.append(custom_number)
    with open ('courier.csv', 'a', newline= '') as additem:
        new_line = csv.writer(additem)
        new_line.writerow(add_courier_name)
    open_a_csv()
    

def update_csv(): 
    with open ('courier.csv', 'r') as file:
        read = csv.DictReader(file)
        courier_list = list(read)
        Name_list = [sub['Name'] for sub in courier_list]
        Phone_list = [sub['Phone'] for sub in courier_list]
        for n, p, in enumerate(zip(Name_list, Phone_list)):
            print(n, p)
    index_pick = int(input("""
Alright Boss, which idiot do you want to change?
    """))
    value_pick = input( "What do you want to change,  Name or Phone?")
    update = input("to?") 
    courier_list[int(index_pick)][value_pick] = update
    titles = ['Name', 'Phone']

    with open ('courier.csv', 'w') as file:
        write = csv.DictWriter(file, fieldnames= titles) 
        write.writeheader() 
        write.writerows(courier_list)
    open_a_csv()



def delete_csv():
    with open ('courier.csv', 'r') as file:
        read = csv.DictReader(file)
        courier_list = list(read)
        Name_list = [sub['Name'] for sub in courier_list]
        Phone_list = [sub['Phone'] for sub in courier_list]
        for n, p, in enumerate(zip(Name_list, Phone_list)):
            print(n, p)
    index_pick = int(input("""
Alright Boss, which idiot do you want to delete?
    """))
    del courier_list[int(index_pick)]
    titles = ['Name', 'Phone']

    with open ('courier.csv', 'w') as file:
        write = csv.DictWriter(file, fieldnames= titles) 
        write.writeheader() 
        write.writerows(courier_list)
    open_a_csv()



