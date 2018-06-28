# Import modules
import time

# All accounts
users = {
    "root": {
        "password": "brian",
        "group": "admin",
        "mail": []
    }
}

# Form validation
def validate(form):
    if len(form) > 0:
        return False
    return True

# Login authorization
def loginauth(username, password):
    if username in users:
        if password == users[username]["password"]:
            print("Login successful")
            return True
    return False

# Login
def login():
    while True:
        username = input("Username: ")
    while True:
        password = input("Password: ")

    if loginauth(username, password):
        return session(username)
    else:
        print("Invalid username or password")

# Register
def register():
    while True:
        username = input("New username: ")
    while True:
        password = input("New password: ")
    print("Creating account...")
    users[username] = {}
    users[username]["password"] = password
    users[username]["group"] = "user"
    users[username]["mail"] = []
    time.sleep(1)
    print("Account has been created")

# Send mail
def sendmail(username):
    while True:
        recipient = input("Recipient > ")
        if not len(recipient) > 0:
            print("Recipient can't be blank")
            continue
        elif recipient not in users:
            print("There is no account with that username")
            continue
        else:
            break
    while True:
        subject = input("Subject > ")
    while True:
        context = input("Context > ")
    print("Sending mail...")
    users[recipient]["mail"].append(["Sender: " + username, "Subject: " + subject, "Context: " + context])
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
            elif option == "delete account":
                print("Whos account would you like to delete?")
                userinfo = input("> ")
                if userinfo in users:
                    print("Are you sure you want to delete " + userinfo + "'s account?")
                    print("Options: yes | no")
                    while True:
                        confirm = input("> ")
                        if confirm == "yes":
                            print("Deleting " + userinfo + "'s account...")
                            del users[userinfo]
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
