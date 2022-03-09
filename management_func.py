#employee id

def employee_id():
    while True:
        id = input("Please enter the employee ID: ")
        if id.isdigit():
            id = int(id)
            return id


#functions for name entry
def name_entry(text = ""):
    while True:
        name = input(f"Please enter {text} name")
        if len(name.strip()) > 1:
            return name

#birth year
def birth_year():
    while True:
        date = input("Please enter the birthyear:")
        if date.isdigit():
            date = int(date)
            if 1900 < date < 2004:
                return int(date)

#birth month
def birth_month():
    while True:
        date = input("Please enter the birth month:")
        if date.isdigit():
            date = int(date)
            if date in range(1, 13):
                return int(date)


#birth day
def birth_day():
    while True:
        date = input("Please enter the day of birth:")
        if date.isdigit():
            date = int(date)
            if date in range(1, 32):
                return int(date)

#position
def position():
    while True:
        name = input(f"Please enter position of employee")
        return name

#whether graduated from uni (boolean)
def uni():
    while True:
        graduate = input("Did the employee graduate from uni? y/n")
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

students = {}

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









