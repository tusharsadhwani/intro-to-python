"""To install this module, run `pip install terminaltables` in your console"""
from terminaltables import AsciiTable


def print_table(employees):
    t = AsciiTable([
        ['Employee Name', 'Employee Salary'],

        *[(emp['name'], emp['salary']) for emp in employees]
    ])

    print(t.table)


employees = []
while True:
    # Ask for a command
    print('''Choose:
    1. View employees
    2. Add employee
    3. Exit
    ''')

    inp = input('> ')
    inp = int(inp)

    # Execute that command
    if (inp == 1):
        print('Current Employees:')
        # for emp in employees:
        #     print(emp['name'], '-', emp['salary'])

        # print('-------------------------------------')
        print_table(employees)

    elif inp == 2:
        emp_name = input('Enter employee name: ')
        emp_salary = float(input('Enter employee salary: '))

        new_employee = {'name': emp_name, 'salary': emp_salary}
        employees.append(new_employee)

    else:
        exit()
