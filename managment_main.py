import management_func

if __name__ == "__main__":

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
            print(management_func.view_total())


        elif selection == 4:
            while True:
                management_func.list_employee()
                break
            #list of employees

        elif selection == 5:#retrieve data of employee by ID
            while True:
                management_func.retrieve_employee()
                break

        elif selection == 6:#Update employees data
            while True:
                management_func.update_employee()
                break

        elif selection == 7:
            break

        else:
            print("invalid input")
            continue