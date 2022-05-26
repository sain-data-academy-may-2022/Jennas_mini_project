import json
import getpass

with open('logins.json') as file:
    logins_list = json.load(file)

def show_list():
    for index,name, in enumerate(logins_list):
                print(index,name,)

def logins_list_fun():
    logins_options = input(""" Logins Menu 
    (0) Exit
    (1) Show current logins
    (2) Add a login
    (3) Update login details. 
    (4) Delete a login.""")
    
    if (logins_options == '0'): 
        print("See ya")
        
    if (logins_options == '1'):
        show_list()
        logins_list_fun()
        
    if (logins_options == '2'):
        username = input("what username do you want")
        password = input("what is your password")
        Accounts = {}
        Accounts ["Username"] = (username)
        Accounts ["Password"] = (password)
        logins_list.append(Accounts)
        show_list()
        logins_list_fun()
        

    if (logins_options =='3'):
        show_list()
        Account_update = int(input("Please selected the number of the account you want to update"))
        for key, value in logins_list[Account_update].items():
            new_info = input(f'Is it {key}? If by some miracle they have actually got it right just press enter, if not what do we need to change it to? >')
            if new_info == "":
                continue
            else:
                logins_list[Account_update][key] = new_info
        show_list()
        logins_list_fun()

    if (logins_options == '4'):  
        show_list()
        delete_login = int(input("Alright, who's left now then? What login is it?"))
        del logins_list [delete_login]
        show_list()
        logins_list_fun()
        
        print('and you never have to think of them again!')

    with open("logins.json", "w") as file:
                json.dump(logins_list, file, indent=4) 