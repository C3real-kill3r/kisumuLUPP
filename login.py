import time

users = {}
option = ""
 
def promptMenu():
    option = input("welcom to Brytech!\nregister | login\n")
    if option == "login":
        existingUser()
    elif option == "register":
        newUser()
#reistration 
def newUser():
    createLogin = input("Enter username: ")
 
    if createLogin in users:
        print("\nLogin name already exist!\n")
    else:
        createPassword = input("New password: ")
        users[createLogin] = createPassword
        print("creating user account...")
        time.sleep(1)
        print("Account succesfully created!!\n")
        
#login an existing user 
def existingUser():
    login = input("Enter username: ")
    password = input("Enter password: ")
    
 
    if login in users and users[login] == password:
        print("\nLogin successful!\n")
    else:
        print("\n login unsuccesful, check username and password\n")
#exiting system
while option != "exit":
    promptMenu()
