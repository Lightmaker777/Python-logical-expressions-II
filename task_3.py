# Task 3

users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            },
            {
                "title": "Python basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan",
        "modules": [
            {
                "title": "Computer basics",
                "completed": False
            }
        ]
    },
    {
        "name": "Luke",
        "type": "Student",
        "password": "skywalker",
        "modules": [
            {
                "title": "Computer basics",
                "completed": True
            }
        ]
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]

modules = [
    {
        "name": "Computer basics"
    },
    {
        "name": "Python basics",
        "requirement": "Computer basics"
    },
    {
        "name": "Django",
        "requirement": "Python basics"
    }
]

def show_registration(username, password, modulename):
    for user in users:
        if user["name"] == username and user["password"] == password:
            if user["type"] == "Student":
                for module in user["modules"]:
                    if module["title"] == modulename:
                        print(f"You are registered to the module {modulename}.")
                        return
                print(f"You did not register to the module {modulename}.")
                return
            elif user["type"] == "Teacher":
                print("You are a teacher.")
                return

def has_completed_module(username, password, modulename):
    for user in users:
        if user["name"] == username and user["password"] == password:
            if user["type"] == "Student":
                for module in user["modules"]:
                    if module["title"] == modulename:
                        if module.get("completed", False):
                            print(f"You have completed the module {modulename}.")
                            return
                        else:
                            print(f"You did not complete the module {modulename}.")
                            return
                print(f"You did not register to the module {modulename}.")
                return
            elif user["type"] == "Teacher":
                return

def may_enroll(username, password, modulename):
    def is_anonymous():
        for user in users:
            if user["name"] == username and user["password"] == password:
                return False
        return True

    def has_no_requirement():
        for module in modules:
            if module["name"] == modulename and "requirement" not in module:
                return True
        return False

    def meets_requirement():
        for module in modules:
            if module["name"] == modulename and "requirement" in module:
                requirement = module["requirement"]
                for user in users:
                    if user["name"] == username and user["password"] == password:
                        if "modules" in user:
                            for user_module in user["modules"]:
                                if user_module["title"] == requirement and user_module.get("completed", False):
                                    return True
                return False

    if is_anonymous() and has_no_requirement():
        return True
    elif not is_anonymous() and (has_no_requirement() or meets_requirement()):
        return True
    else:
        return False

# Test the functions
username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")

# Check if the user exists
user_exists = False
for user in users:
    if user["name"] == username and user["password"] == password:
        user_exists = True
        break

# Perform the required actions based on user existence
if user_exists:
    show_registration(username, password, modulename)
    has_completed_module(username, password, modulename)
    if may_enroll(username, password, modulename):
        print(f"You may register to the module {modulename}.")
    else:
        print(f"You may not register to the module {modulename}.")
else:
    print("User not found or invalid credentials")
