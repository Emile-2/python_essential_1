number_of_employees = input("Enter the amount of employees you have: ")
number_of_employees_int = int(number_of_employees)
ages = []
employees = 1

while number_of_employees_int >= employees:
    print(f"\nEnter details for employee {employees}")

    first_name = input("Enter employees first name: ")

    if first_name.strip():
        print("Success")
    else:
        print(f'\nUnrecognized input, Please enter employee {employees}\'s details again')
        continue

    last_name = input("\nEnter employees last name: ")

    if last_name.strip():
        print("Success")
    else:
        print(f'\nUnrecognized input, Please enter employee {employees}\'s details again')
        continue

    age = input("Enter employees age: ")

    if int(age) >= 18 and int(age) <= 100:
        print("\nSuccess")
        ages.append(int(age))

    else:
        print(f'\nUnrecognized input, Please enter employee {employees}\'s details again')
        continue

    employees += 1

    print(f"\n{first_name} {last_name} is {age} years old")

if sum(ages) > 500:
    print(f"The sum of all ages is {sum(ages)}")




