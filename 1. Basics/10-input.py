# How to take user input in python:

input_string = input('Enter your age: ')
age = int(input_string)

if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teenager')
    print('You will be an adult in', 18-age, 'years')
else:
    print('You are a child')
