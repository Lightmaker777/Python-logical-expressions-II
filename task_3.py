# Task 3

users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter",
        "modules": [
            {"title": "Computer basics", "completed": True},
            {"title": "Python basics", "completed": False}
        ]
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan",
        "modules": [
            {"title": "Computer basics", "completed": False}
        ]
    },
    {
        "name": "Luke",
        "type": "Student",
        "password": "skywalker",
        "modules": [
            {"title": "Computer basics", "completed": True}
        ]
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]
# Create a dictionary to store the modules and their requirements
modules = {
    "Computer basics": None,
    "Python basics": "Computer basics",
    "Django": "Python basics"
}
# Define a function to show if a user is registered to a module
def show_registration(username, password, module_name):
    user = find_user(username, password)
    if not user:
        print(f"You did not register to the module {module_name}.")
    elif is_teacher(user):
        print("You are a teacher.")
    elif is_student(user):
        if is_module_registered(user, module_name):
            print(f"You are registered to the module {module_name}.")
        else:
            print(f"You did not register to the module {module_name}.")
# Define a function to show if a user has completed a module
def has_completed_module(username, password, module_name):
    user = find_user(username, password)
    if not user:
        print(f"You did not complete the module {module_name}.")
    elif is_teacher(user):
        return
    elif is_student(user):
        if is_module_completed(user, module_name):
            print(f"You have completed the module {module_name}.")
        else:
            print(f"You did not complete the module {module_name}.")
# Define a function to find a user by name and password
def find_user(username, password):
    for user in users:
        if user["name"] == username and user.get("password") == password:
            return user
    return None
# Define a function to check if a user is a student
def is_student(user):
    return user["type"] == "Student"
# Define a function to check if a user is a teacher
def is_teacher(user):
    return user and user.get("type") == "Teacher"
# Define a function to check if a user is registered to a module
def is_module_registered(user, module_name):
    return module_name in (module["title"] for module in user.get("modules", []))
# Define a function to check if a user has completed a module
def is_module_completed(user, module_name):
    if is_student(user) and is_module_registered(user, module_name):
        for module in user["modules"]:
            if module["title"] == module_name and module.get("completed", False):
                return True
    return False

# Helper function to check if a user is anonymous
def is_anonymous(username):
    return username.lower() == "anonymous"
# Helper function to check if a module has no requirement
def has_no_requirement(module_name):
    return modules.get(module_name) is None
# Helper function to check if a user meets the requirement for a module
def meets_requirement(user, module_name):
    requirement = modules.get(module_name)
    return is_module_registered(user, requirement) and is_module_completed(user, requirement)
# Updated function to check if a user may enroll in a module
def may_enroll(username, password, module_name):
    user = find_user(username, password)
    # Anonymous users are allowed to enroll in modules without requirements
    if is_anonymous(username):
        return has_no_requirement(module_name)
    if not user:
        return False
    if module_name not in modules:
        return False
    if is_student(user) and not is_module_registered(user, module_name):
        return has_no_requirement(module_name) or meets_requirement(user, module_name)
    return False
# Test the functions with user inputs
username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
module_name = input("What module do you want to check? ")
show_registration(username, password, module_name)
has_completed_module(username, password, module_name)
if may_enroll(username, password, module_name):
    print(f"You may register to the module {module_name}.")
else:
    print(f"You may not register to the module {module_name}.")
