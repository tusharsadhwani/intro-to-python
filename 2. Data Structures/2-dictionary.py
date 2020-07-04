# Dictionary: An unordered structure containing key-value pairs
#
# 1. Dictionaries in python don't have a specific data type
# 2. Dictionaries in python don't have a specific size
# 3. Dictionary keys should always be unique
#    (like in a dictionary, any word is only defined once)
# 4. You can use the key to get the value
#    (like in a dictionary, you can use a word to get its meaning)

'''
>>> d = {}
>>> d
{}
>>> d['name'] = 'Suyash'
>>> d
{'name': 'Suyash'}
>>> d['name']
'Suyash'
>>> d['age'] = 23
>>> d
{'name': 'Suyash', 'age': 23}
>>> d['age'] = 25
>>> d 
{'name': 'Suyash', 'age': 25}
>>> del d['name']
>>> d
{'age': 25}
'''

employee_1 = {'name': 'Deepak'}
employee_1['salary'] = 20000.0


def show_salary(emp):
    print('Employee', emp['name'], 'has a salary of Rs.', emp['salary'])


def promotion(emp):
    emp['salary'] = emp['salary'] * 1.2  # 20% raise


show_salary(employee_1)
promotion(employee_1)
show_salary(employee_1)
