# This module provides various functions to manipulate time values.
import time
from users import User

# Form validation
def validate(form):
    if len(form) > 0:
        return False
    return True

def is_user_admin(user):
    return user.group == "admin"

# this checks if the username and password matches what is in the database
def login_authorization(username, password):
    if username in User:
        if password == User[username]["password"]:
            print("Login successful")
            return True
    return False

# Login
def login():
    while True:
        username = input("Username: ")
        break
    while True:
        password = input("Password: ")
        break

    if login_authorization(username, password):
        return session(username)
    else:
        print("Invalid username or password")

# Register
def register():
    while True:
        username = input("New username: ")
        break
    while True:
        password = input("New password: ")
        break
    print("Creating account...")
    User[username] = {}
    User[username]["password"] = password
    User[username]["group"] = "user"
    User[username]["mail"] = []
    time.sleep(1)
    print("Account has been created")

# Send mail
def sendmail(username):
    while True:
        recipient = input("Recipient > ")
        break
    while True:
        subject = input("Subject > ")
        break
    while True:
        comment = input("Comment > ")
        break
    print("Sending mail...")
    User[recipient]["mail"].append(["Sender: " + username, "Subject: " + subject, "Comment: " + comment])
    time.sleep(1)
    print("Mail has been sent to " + recipient)

# User session
def session(username):
    print("Welcome to your account " + username)
    print("Options: view mail | send mail | logout")
    if User[username]["group"] == "admin":
        print("")
    while True:
        option = input(username + " > ")
        if option == "logout":
            print("Logging out...")
            break
        elif option == "view mail":
            print("Current mail:")
            for mail in User[username]["mail"]:
                print(mail)
        elif option == "send mail":
            sendmail(username)
        elif User[username]["group"] == "admin":
            if option == "user mail":
                print("Whos mail would you like to see?")
                userinfo = input("> ")
                if userinfo in User:
                    for mail in User[userinfo]["mail"]:
                        print(mail)
                else:
                    print("There is no account with that username")
            elif option == "delete mail":
                print("Whos mail would you like to delete?")
                userinfo = input("> ")
                if userinfo in User:
                    print("Deleting " + userinfo + "'s mail...")
                    User[userinfo]["mail"] = []
                    time.sleep(1)
                    print(userinfo + "'s mail has been deleted")
                else:
                    print("There is no account with that username")
            elif option == "delete account":
                print("Whos account would you like to delete?")
                userinfo = input("> ")
                if userinfo in User:
                    print("Are you sure you want to delete " + userinfo + "'s account?")
                    print("Options: yes | no")
                    while True:
                        confirm = input("> ")
                        if confirm == "yes":
                            print("Deleting " + userinfo + "'s account...")
                            del User[userinfo]
                            time.sleep(1)
                            print(userinfo + "'s account has been deleted")
                            break
                        elif confirm == "no":
                            print("Canceling account deletion...")
                            time.sleep(1)
                            print("Account deletion canceled")
                            break
                        else:
                            print(confirm + " is not an option")
                else:
                    print("There is no account with that username")
        else:
            print(option + " is not an option")

# On start
print("Welcome to the system. Please register or login.")
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

# On exit
print("Shutting down...")
time.sleep(1)
