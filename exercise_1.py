#This is app is designed for data entry

no_employees = input("Enter the amount of employees you have: ")
no_employees_int = int(no_employees)
ages = []
employees = 1

while no_employees_int >= employees:

    print(f"\nEnter details for employee {employees}")
    first_name = input("Enter employees first name: ")

    if first_name.strip():
        print("\nSuccess")
    else:
        print('\nUnrecognized input, Start over')
        continue

    last_name = input("\nEnter employees last name: ")
    if last_name.strip():
        print("\nSuccess")
    else:
        print('\nUnrecognized input, Start over')
        continue

    age = input("\nEnter employees age: ")

    if int(age) >= 18 and int(age) <= 100:
        print("\nSuccess")
        ages.append(int(age))
    else:
        print('\nUnrecognized input, Start over')
        continue

    employees += 1

    print(f"\n{first_name} {last_name} is {age} years old")


if sum(ages) > 500:
    print(f"The sum of all ages is {sum(ages)}")




