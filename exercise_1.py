#This is app is designed for data entry

#
no_employees = input("Enter the amount of employees you have: ")
#
no_employees = int(no_employees)

ages = []


for index in range(no_employees):
    first_name = input("Enter employees first name: ")

    if first_name.rstrip():
            print("Success")

    else:
        print('Unrecognized input')
        continue


    last_name = input("Enter employees last name")
    if last_name.rstrip():
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

print(sum(ages))




