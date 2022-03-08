# create operations
def operation_list():
    print("""
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exit
          """)

def add(number_one, number_two):
    return f"{number_one} + {number_two} = {number_one + number_two}"

def subtract(number_one, number_two):
    return f"{number_one} - {number_two} = {number_one - number_two}"

def multiply(number_one, number_two):
    return f"{number_one} x {number_two} = {number_one * number_two}"

def divide(number_one, number_two):
    return f"{number_one} / {number_two} = {number_one / number_two}"

def number_one():
    while True:
        number_str = input("Please enter first number: ")
        if number_str.isdigit():
            return int(number_str)

def number_two():
    while True:
        number_str = input("Please enter second number: ")
        if number_str.isdigit():
            return int(number_str)

if __name__ =='__main__':
    while True:
        first_number = number_one()
        second_number = number_two()
        break


    while True:
        # get input for operation selected
        operation_list()

        #i orginally forgot to cast this input to an int, causing issues
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



