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
                #print("You are a teacher")
                return
    # If the loop completes without finding a matching user
    print("You did not register to the module " + modulename)
    print("You did not complete the module " + modulename) 

# the function will do nothing if the user is valid and a teacher.
# It will check if, besides having a particular module in the user's list, the module has the key completed set to True.
def has_completed_module(username, password, modulename):
    for user in users:
        if user["name"] == username and user["password"] == password:
            if user["type"] == "Student":
                for module in user["modules"]:
                    if module["title"] == modulename:
                        if module.get("completed", False):
                            print("You have completed the module " + modulename)
                        else:
                            print("You did not complete the module " + modulename)
                            return
                    else:    
                        print("You did not register to the module " + modulename)
                        return
            elif user["type"] == "Teacher":
                return                 
    
           
# Test the functions
username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")
show_registration(username, password, modulename)
has_completed_module(username, password, modulename)

