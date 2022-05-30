import json
from csv_fun import show_csv, courier_list, create_a_csv


with open('couriers.json') as file:
    Courier_list = json.load(file)

def show_list():
    for index,name, in enumerate(Courier_list):
                print(index,name,)
    with open("couriers.json", "w") as file:
                json.dump(Courier_list, file)

    
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
            show_list() 
            Courier_list_fun()
            break
            

        #add a courier 
        if (courier_options == '2'):
            courier_update = (input('add courier name '))
            Courier_list.append(courier_update)
            show_list()
            Courier_list_fun()
            break
            

        #update couriers details 
        if (courier_options =='3'):
            show_list()
            courier_update = int(input('Please choose number of courier you want to update'))
            update = input('what would you like to update it to?')
            Courier_list[courier_update] = update
            show_list()
            Courier_list_fun()
            break

        #delete a courier 

        if (courier_options =='4'):
            show_list()
            courier_update = int(input('Please choose number of courier you want to delete'))
            del Courier_list [courier_update]
            show_list()
            Courier_list_fun()
            break

        else:
            print("""
            Come on mate, I know we have bad days, but this.....TRY AGAIN""")




