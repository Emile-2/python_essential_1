#This is app is designed for data entry

no_employees = input("Enter the amount of employees you have: ")
no_employees_int = int(no_employees)
ages = []
employees = 0

while no_employees_int >= employees:

    print(f"Enter details for employee {employees + 1}")
    first_name = input("Enter employees first name: ")

    if first_name.strip():
        print("Success")
    else:
        print('Unrecognized input')
        continue

    last_name = input("Enter employees last name")
    if last_name.strip():
        print("Success")
    else:
        print('Unrecognized input')
        continue

    age = input("Enter employees age")

    if int(age) >= 18 and int(age) <= 100:
        print("Success")
        ages.append(int(age))
    else:
        print('Unrecognized input')
        continue

    employees += 1

    print(f"{first_name} {last_name} is {age} years old")

print(sum(ages))




