#employee id
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
    while True:

        data_choices_str = input("""
        Which data would you like to update?
        1. First Name
        2. Last Name
        3. Year of Birth
        4. Month of Birth
        5. Day of Birth
        6. Position
        7. Graduated
        8. ID
        9. Exit
        """)

        if data_choices_str.isdigit() and data_update_str in range(1, 10):
            data_choices = int(data_choices_str)

            if data_choices == 1:
                return 1
            elif data_choices == 2:
                return 2
            elif data_choices == 3:
                return 3
            elif data_choices == 4:
                return 4
            elif data_choices == 5:
                return 5
            elif data_choices == 6:
                return 6
            elif data_choices == 7:
                return 7
            elif data_choices == 8:
                return 8
            elif data_choices == 9:
                return 9


def employee_id():
    while True:
        id = input("Please enter the employee ID: ")
        if id.isdigit():
            id = int(id)
            return id


#functions for name entry
def name_entry(text = ""):
    while True:
        name = input(f"Please enter {text}: ")
        if len(name.strip()) > 1:
            return name

#birth year
def birth_year():
    while True:
        date = input("Please enter the birthyear: ")
        if date.isdigit():
            date = int(date)
            if 1900 < date < 2004:
                return int(date)

#birth month
def birth_month():
    while True:
        date = input("Please enter the birth month: ")
        if date.isdigit():
            date = int(date)
            if date in range(1, 13):
                return int(date)


#birth day
def birth_day():
    while True:
        date = input("Please enter the day of birth: ")
        if date.isdigit():
            date = int(date)
            if date in range(1, 32):
                return int(date)

#position
def position():
    while True:
        name = input(f"Please enter position of employee: ")
        return name

#whether graduated from uni (boolean)
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

#create a dictionary

#populate dictionary with dictionary of values
#employee id as key, information as value


def add_employees():

    while True:
        id = employee_id()

        students[f"{id}"] = {}
        print(students)

        students[f"{id}"]["first_name"] = f"{name_entry('First Name')}"
        print(students)

        students[f"{id}"]["last_name"] = f"{name_entry('Last Name')}"
        print(students)

        students[f"{id}"]["birth_year"] = f"{birth_year()}"
        print(students)

        students[f"{id}"]["birth_month"] = f"{birth_month()}"
        print(students)

        students[f"{id}"]["birth_day"] = f"{birth_day()}"
        print(students)

        students[f"{id}"]["position"] = f"{position()}"
        print(students)

        students[f"{id}"]["graduated"] = f"{uni()}"
        print(students)

def del_employee():
    print(students)
    while True:
        id_del_str = input("Enter ID of student you would like to remove, Press Q to go back")

        if id_del_str.isdigit():
            id_del = int(id_del_str)
            # print(f"Employee {students[id_del]} has been deleted")
            print(students.pop(id_del, "Key does not exist"))


        elif id_del_str.isalpha() and id_del_str.capitalize() == "Q":
            break

def retrieve_employee():

    while True:
        data_retrieve_str = input("Please enter the ID of the employees you would like to view, press Q to go back")
        if data_retrieve_str.isdigit():
            try:
                data_retrieve = int(data_retrieve_str)
                print(students[data_retrieve])
            except KeyError:
                print("Id incorrect")

        elif data_retrieve_str.isalpha() and data_retrieve_str.capitalize() == "Q":
            break



if __name__ == "__main__":
    students = {1:{"name":"emile",
               "age": 30,
            "city": "birmingham"}
                }
    while True:
        selection = menu()


        if selection == 1: #add employee option
            while True:
                add_employees()
                break

        elif selection == 2: #delete employee option
            while True:
                del_employee()
                break

        elif selection == 3:#View total number of employees

            print(f"There is a total of {len(students.keys())} employees" )

        elif selection == 4:
            pass#list of employees

        elif selection == 5:#retrieve data of employee by ID
            while True:
                retrieve_employee()
                break

        elif selection == 6:#Update employees data

            while True:
                data_update_str = input("Enter the ID of the Employee you would like to update: ")
                if data_update_str.isdigit():
                    data_update = int(data_update_str)
                    print(students[data_update])
                    data_choice = data_choice()
                    print(students[data_update][data_choice()])














        if selection == 7:
            break










