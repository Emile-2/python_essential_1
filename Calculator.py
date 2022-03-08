# create operations
def operation_list():
    print("""
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exit
          """)
#add function
def add(number_one, number_two):
    return f"{number_one} + {number_two} = {number_one + number_two}"

def subtract(number_one, number_two):
    return f"{number_one} - {number_two} = {number_one - number_two}"

def multiply(number_one, number_two):
    return f"{number_one} x {number_two} = {number_one * number_two}"

def divide(number_one, number_two):
    return f"{number_one} / {number_two} = {number_one / number_two}"

def number_one(text):
    while True:
        number_str = input(f"Please enter {text} number: ")
        if number_str.isdigit():
            return float(number_str)

def calc_main():

    while True:
        # get input for operation selected
        operation_list()

        operation_str = input("Please select which operation: ")
        if operation_str.isdigit():
            operation = int(operation_str)

            if operation == 1:
                print(add(first_number, second_number))
                continue

            elif operation == 2:
                print(subtract(first_number, second_number))
                continue

            elif operation == 3:
                print(multiply(first_number, second_number))
                continue

            elif operation == 4:
                print(divide(first_number, second_number))
                continue

            elif operation == 5:
                print("Thanks for using the calculator")
                break

        else:
            print("Unknown input")

if __name__ =='__main__':

    while True:
        first_number = number_one("first")
        second_number = number_one("second")
        break

    while True:
        calc_main()
        break
