# ask user for input of two integers

# create operations
def operation_list():
    print("""1. Add
          2. Subtract
          3. Multiply
          4. Divide
          5. Exit
          """)

def add(number_one, number_two):
    return number_one + number_two

def subtract(number_one, number_two):
    return number_one - number_two

def multiply(number_one, number_two):
    return number_one * number_two

def divide(number_one, number_two):
    return number_one / number_two


#get input for numbers
first_number_str = input("Please enter first number: ")
second_number_str = input("please enter second number")

#get input for operation selected


first_number = int(first_number_str)
second_number = int(second_number_str)


if __name__ =='__main__':
    while True:
        operation_list()
        #i orginally forgot to cast this input to an int, causing issues
        operation_str = input("Please select which operation")
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








#


