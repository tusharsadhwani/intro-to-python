# Practical examples of what we have learned so far:

# 1. generating a set of prime numbers

# upper_limit = 100
# primes = set()

# for n in range(2, upper_limit):
#     primes.add(n)  # assume it is a prime
#     for p in primes:
#         # if n is divisible by a prime (other than itself):
#         if n % p == 0 and n != p:
#             primes.remove(n)
#             break  # we know it's not a prime so we can stop the loop

# print(primes)


# 2. Employee directory:

# employees = []
# while True:
#     # Ask for a command
#     print('''Choose:
#     1. View employees
#     2. Add employee
#     3. Exit
#     ''')

#     inp = input('> ')
#     inp = int(inp)

#     # Execute that command
#     if (inp == 1):
#         print('Current Employees:')
#         for emp in employees:
#             print(emp['name'], '-', emp['salary'])

#         print('-------------------------------------')

#     elif inp == 2:
#         emp_name = input('Enter employee name: ')
#         emp_salary = float(input('Enter employee salary: '))

#         new_employee = {'name': emp_name, 'salary': emp_salary}
#         employees.append(new_employee)

#     else:
#         exit()
