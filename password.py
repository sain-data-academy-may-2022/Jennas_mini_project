import getpass 
login = {
    'mgr001' : '8055'
}

def password():
   while(True):
    username = input('usernam : ')
    password = getpass.getpass('password :')
    if username in login and login[username]==password:
        print('Manager Menu', username) 
        break
    else:
        print("Incorrect, you aint the govenor are you!")
    
    