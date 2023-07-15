# Task 1
# a function named show_registration that checks if a user is registered to a specific module.
# The function will accept three input arguments: username(string), password(string), modulename(string)

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
def show_registration(username, password, modulename):
    for user in users:
        if user["name"] == username and user["password"] == password:
            if user["type"] == "Student":
                for module in user["modules"]:
                    if module["title"] == modulename:
                        print("You are registered to the module " + modulename)
                        return
                  
                    print("You did not register to the module " + modulename)
                    return
            elif user["type"] == "Teacher":                
                print("You are a teacher")
                return
    # If the loop completes without finding a matching user
    print("User not found or invalid credentials")
                
# codes to test:
username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")
show_registration(username, password, modulename)