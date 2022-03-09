# employee id

employees = {1:{"first_name":"emile",
                "last_name" : "thompson",
                "birth_year" : 1991,
                "birth_month" : 8,
                "birth_day" : 12,
                "position" : "unknown",
                "graduated" : True
                },
            2: {"first_name":"ben",
                "last_name" : "shield",
                "birth_year" : 1981,
                "birth_month" : 2,
                "birth_day" : 16,
                "position" : "unknown",
                "graduated" : True
                }}


def menu():
    selection = input("""
    1. Add new employee
    2. Delete an employee
    3. View total number of employees
    4. List of employees
    5. Retrieve data of employee by ID
    6. Update employees data
    7. Exit: 
    """)
    if selection.isdigit() and int(selection) in range(1, 8):
        return int(selection)


def data_choice():
    # while True:

    print("""
        Which data would you like to update?
        1. First Name
        2. Last Name
        3. Year of Birth
        4. Month of Birth
        5. Day of Birth
        6. Position
        7. Graduated
        8. Exit
        """)



    # if data_choices_str.isdigit() and data_choices_str in range(1, 10):
    #     data_choices = int(data_choices_str)
    #
    #     if data_choices == 1:
    #         choice = "first_name"
    #
    #     # elif data_choices == 2:
    #     #     return "last_name"
    #     # elif data_choices == 3:
    #     #     return 3
    #     # elif data_choices == 4:
    #     #     return 4
    #     # elif data_choices == 5:
    #     #     return 5
    #     # elif data_choices == 6:
    #     #     return 6
    #     # elif data_choices == 7:
    #     #     return 7
    #     # elif data_choices == 8:
    #     #     return 8
    #     # elif data_choices == 9:
    #     #     return 9
    #     return choice
    #     print(choice)


def employee_id():
    while True:
        id = input("Please enter the employee ID: ")
        if id.isdigit():
            id = int(id)
            return id


# functions for name entry
def name_entry(text=""):
    while True:
        name = input(f"Please enter {text}: ")
        if len(name.strip()) > 1:
            return name


# birth year
def birth_year():
    while True:
        date = input("Please enter the birthyear: ")
        if date.isdigit():
            date = int(date)
            if 1900 < date < 2004:
                return int(date)


# birth month
def birth_month():
    while True:
        date = input("Please enter the birth month: ")
        if date.isdigit():
            date = int(date)
            if date in range(1, 13):
                return int(date)


# birth day
def birth_day():
    while True:
        date = input("Please enter the day of birth: ")
        if date.isdigit():
            date = int(date)
            if date in range(1, 32):
                return int(date)


# position
def position():
    while True:
        name = input(f"Please enter position of employee: ")
        return name


# whether graduated from uni (boolean)
def uni():
    while True:
        graduate = input("Did the employee graduate from uni? y/n: ")
        if graduate.isalpha() and len(graduate) == 1:
            if graduate.capitalize() == "Y":
                return True
            elif graduate.capitalize() == "N":
                return False
            else:
                continue


# create a dictionary

# populate dictionary with dictionary of values
# employee id as key, information as value


def add_employees():
    while True:

        id = employee_id()

        employees[f"{id}"] = {}

        employees[f"{id}"]["first_name"] = f"{name_entry('First Name')}"

        employees[f"{id}"]["last_name"] = f"{name_entry('Last Name')}"

        employees[f"{id}"]["birth_year"] = f"{birth_year()}"

        employees[f"{id}"]["birth_month"] = f"{birth_month()}"

        employees[f"{id}"]["birth_day"] = f"{birth_day()}"

        employees[f"{id}"]["position"] = f"{position()}"

        employees[f"{id}"]["graduated"] = f"{uni()}"

        return employees


def del_employee():
    print(employees)
    while True:
        id_del_str = input("Enter ID of student you would like to remove, Press Q to go back")

        if id_del_str.isdigit():
            id_del = int(id_del_str)
            # print(f"Employee {employees[id_del]} has been deleted")
            employees.pop(id_del, "Key does not exist")


        elif id_del_str.isalpha() and id_del_str.capitalize() == "Q":

            break
def list_employee():
    main_key = employees.keys()

    for keys in main_key:
        first = employees[keys]["first_name"]
        last = employees[keys]["last_name"]
        print(f"{first} {last}")

def retrieve_employee():
    while True:
        data_retrieve_str = input("Please enter the ID of the employees you would like to view, press Q to go back")
        if data_retrieve_str.isdigit():
            try:
                data_retrieve = int(data_retrieve_str)
                print(employees[data_retrieve])
            except KeyError:
                print("Id incorrect")

        elif data_retrieve_str.isalpha() and data_retrieve_str.capitalize() == "Q":
            break

        # if selection == 7:
        #     break
def view_total():
    total_employees = len(employees.keys())
    return f"There are {total_employees} employees"

def update_employee():

    while True:
        data_update_str = input("Enter the ID of the Employee you would like to update, or type Q to quit: ")
        #if you put in the correct id move on
        if data_update_str.isdigit():
            data_update = int(data_update_str)
            try:
                #show info on id that was entered
                print(employees[data_update])

            except KeyError:
                print("unrecognized ID")

            data_choice()
            choice_str = input("Please enter option number, or type Q to exit: ")
            if choice_str.isdigit() and int(choice_str) in range(1, 10):
                choice = int(choice_str)


                if choice == 1:
                    option = "first_name"
                    print(employees[data_update][option])
                    change = name_entry("New First Name")
                    employees[data_update][option] = change
                    print(employees[data_update])
                    continue

                elif choice == 2:
                    option = "last_name"
                    print(employees[data_update][option])
                    change = name_entry("Enter new Last Name")
                    employees[data_update][option] = change
                    print(employees[data_update])
                    continue


                elif choice == 3:
                    option = "birth_year"
                    print(employees[data_update][option])
                    change = birth_year()
                    employees[data_update][option] = change
                    print(employees[data_update])
                    continue

                elif choice == 4:
                    option = "birth_month"
                    print(employees[data_update][option])
                    change = birth_month()
                    employees[data_update][option] = change
                    print(employees[data_update])
                    continue

                elif choice == 5:
                    option = "birth_day"
                    print(employees[data_update][option])
                    change = birth_day()
                    employees[data_update][option] = change
                    print(employees[data_update])
                    continue

                elif choice == 6:
                    option = "position"
                    print(employees[data_update][option])
                    change = position()
                    employees[data_update][option] = change
                    print(employees[data_update])
                    continue

                elif choice == 7:
                    option = "graduated"
                    print(employees[data_update][option])
                    change = uni()
                    employees[data_update][option] = change
                    print(employees[data_update])
                    continue

                elif choice == 8:
                    break

            elif choice_str.upper() == "Q":
                break
        elif data_update_str.capitalize() == "Q":
            break


    return f"There is a total of {len(employees.keys())} employees"


