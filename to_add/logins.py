import json
import getpass

with open('logins.json', "r") as file:
    usernames = json.load(file)

with open('passwords.json', "r") as file:
    passwords = json.load(file)


def show_list():
    for index,name, in enumerate(usernames):
        print(index,name,)
    with open("logins.json", "w") as file:
        json.dump(usernames, file ) 
    with open("passwords.json", "w") as file:
        json.dump(passwords, file ) 

def logins_list_fun():
    while(True):
    
        logins_options = input(""" Logins Menu 
        (0) Exit
        (1) Show current logins
        (2) Add a login
        (3) Update login details. 
        (4) Delete a login.""")
        
        if (logins_options == '0'): 
            print("See ya")
            break
            
        if (logins_options == '1'):
            show_list()
            logins_list_fun()
            break
            
            
        if (logins_options == '2'):
            username = input("what username do you want? ")
            password = int(input("what is your password? "))
            usernames.append(username)
            passwords.append(password)
            show_list()
            logins_list_fun()
            break
            

        if (logins_options =='3'):
            show_list()
            Account_update = int(input("Please selected the number of the login you want to update? If its the pass work you want to change just press enter "))
            change = input(f"What do you want to change {usernames[Account_update]} to?")
            if change == '':
                pass
            else:
                usernames[Account_update] = change
            password_update = int(input("Do you want to change the password too? If not leave it blank? "))
            if password_update == "":
                pass
            else:
                passwords[Account_update] = password_update
            show_list()
            logins_list_fun()
            break

        if (logins_options == '4'):  
            show_list()
            delete_login = int(input("Alright, who's left now then? What login is it?"))
            del usernames[delete_login]
            del passwords[delete_login]
            show_list()
            logins_list_fun()
            break
            
            print('and you never have to think of them again!')

        else:
            print("Oi, if you carry on like this I'll fire you!")

