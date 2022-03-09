import management_func

if __name__ == "__main__":
    students = {1:{"name":"emile",
               "age": 30,
            "city": "birmingham"}
                }
    while True:
        selection = management_func.menu()


        if selection == 1: #add employee option
            while True:
                management_func.add_employees()
                break

        elif selection == 2: #delete employee option
            while True:
                management_func.del_employee()
                break

        elif selection == 3:#View total number of employees

            print(f"There is a total of {len(students.keys())} employees" )

        elif selection == 4:
            pass#list of employees

        elif selection == 5:#retrieve data of employee by ID
            while True:
                management_func.retrieve_employee()
                break

        elif selection == 6:#Update employees data

            while True:
                data_update_str = input("Enter the ID of the Employee you would like to update: ")
                if data_update_str.isdigit():
                    data_update = int(data_update_str)
                    print(students[data_update])
                    data_choice = data_choice()
                    print(students[data_update][data_choice()])