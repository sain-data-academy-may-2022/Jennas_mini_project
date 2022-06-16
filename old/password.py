import getpass 
#Alex code - with adjustments ^_^

import json


with open('logins.json', "r") as file:
    usernames = json.load(file)

with open('passwords.json', "r") as file:
    passwords = json.load(file)

def password():
   while(True):
    
    username = input('username : ')
    password = int(getpass.getpass('password :'))
    if (username in usernames):
        pass
    if (password in passwords):
        print(f"""
        Back End. How you doing today {username}?""")
        break
    else:
        print("Incorrect, you aint the govenor are you!")
    



