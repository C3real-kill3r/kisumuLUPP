# This module provides various functions to manipulate time values.
import time
from db import users
from users import User

# Form validation
def validate(form):
    if len(form) > 0:
        return False
    return True

# Login authorization
def login_authorization(username, password):
    if username in users:
        if password == users[username]["password"]:
            print("Login successful")
            return True
    return False

# Login
def login():
    while True:
        username = input("Username: ")
        if not len(username) > 0:
            print("Username can't be blank")
        else:
            break
    while True:
        password = input("Password: ")
        if not len(password) > 0:
            print("Password can't be blank")
        else:
            break
    if login_authorization(username, password):
        return session(username)
    else:
        print("Invalid username or password")

# Register
def register():
    while True:
        username = input("New username: ")
        if not len(username) > 0:
            print("Username can't be blank")
            continue
        else:
            break
    while True:
        password = input("New password: ")
        if not len(password) > 0:
            print("Password can't be blank")
            continue
        else:
            break
    print("Creating account...")
    users[username] = {}
    users[username]["password"] = password
    users[username]["group"] = "user"
    users[username]["email"] = []
    time.sleep(1)
    print("Account has been created")

# Send mail
def sendmail(username):
    while True:
        recipient = input("Recipient > ")
        if recipient not in users:
            print("There is no account with that username")
            continue
        else:
            break
    while True:
        subject = input("Subject > ")
        if not len(subject) > 0:
            print("Subject can't be blank")
            continue
        else:
            break
    while True:
        comment = input("comment > ")
        if not len(comment) > 0:
            print("comment can't be blank")
        else:
            break
    print("Sending mail...")
    users[recipient]["mail"].append(["Sender: " + username, "Subject: " + subject, "Comment: " + comment])
    time.sleep(1)
    print("Mail has been sent to " + recipient)

# User session
def session(username):
    print("Welcome to your account " + username)
    print("Options: view mail | send mail | logout")
    if users[username]["group"] == "admin":
        print("")
    while True:
        option = input(username + " > ")
        if option == "logout":
            print("Logging out...")
            break
        elif option == "view mail":
            print("Current mail:")
            for mail in users[username]["mail"]:
                print(mail)
        elif option == "send mail":
            sendmail(username)
        elif users[username]["group"] == "admin":
            if option == "user mail":
                print("Whos mail would you like to see?")
                userinfo = input("> ")
                if userinfo in users:
                    for mail in users[userinfo]["mail"]:
                        print(mail)
                else:
                    print("There is no account with that username")
            elif option == "delete mail":
                print("Whos mail would you like to delete?")
                userinfo = input("> ")
                if userinfo in users:
                    print("Deleting " + userinfo + "'s mail...")
                    users[userinfo]["mail"] = []
                    time.sleep(1)
                    print(userinfo + "'s mail has been deleted")
                else:
                    print("There is no account with that username")
        else:
            print(option + " is not an option")

# when launching the application
print("!!Welcome to the The Big Adventure!!\n Please register or login.")
print("Options: register | login | exit")
while True:
    option = input("> ")
    if option == "login":
        login()
    elif option == "register":
        register()
    elif option == "exit":
        break
    else:
        print(option + " is not an option")

# when exitting the application
print("Shutting down...")
time.sleep(1)
