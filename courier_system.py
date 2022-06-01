import csv
from courier_csv import open_a_csv, add_an_item_to_csv, update_csv, delete_csv

with open ('courier.csv', 'r') as file:
        read = csv.DictReader(file)
        courier_list = list(read)

        Name = [sub['Name'] for sub in courier_list]
        Phone = [sub['Phone'] for sub in courier_list]


def Courier_list_fun():
    while(True):
        courier_options = input("""
Couriers Menu  
        (0) Exit
        (1) Show current couriers names
        (2) Add Courier
        (3) Update a couriers details. 
        (4) Delete a courier.""")

        #exit 
        
        if (courier_options == '0'): 
            ("See ya")
            break
        
            
        #shows courier list   
        if (courier_options == '1'):
            open_a_csv()
            Courier_list_fun()
            break
            

        #add a courier 
        if (courier_options == '2'):
            add_an_item_to_csv()
            Courier_list_fun()
            break
            

        #update couriers details 
        if (courier_options =='3'):
            update_csv()
            Courier_list_fun()
            break

        #delete a courier 

        if (courier_options =='4'):
            delete_csv()
            Courier_list_fun()
            break

        else:
            print("""
            Come on mate, I know we have bad days, but this.....TRY AGAIN""")




