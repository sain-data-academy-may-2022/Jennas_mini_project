# import json

usernames = ['mgr001', 'mgr002', 'mgr003']
# passwords = [8055, 7734, 1346]

for index,name, in enumerate(usernames):
    print(index,name,)
Account_update = int(input("Please selected the number of the login you want to update"))
change = input(f"What do you want to change {usernames[Account_update]} to?")
usernames[Account_update] = change
print(usernames)