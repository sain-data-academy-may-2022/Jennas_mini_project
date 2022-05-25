import getpass 
login = {
    'Username' : 'mgr001',
    'Password' : '8055'
}

def password():
   while(True):
    username = input('username : ')
    password = getpass.getpass('password :')
    if username == (login['Username']) and password == (login['Password']):
        print('Manager Menu', username) 
        break
    else:
        print("Incorrect, you aint the govenor are you!")
    
    