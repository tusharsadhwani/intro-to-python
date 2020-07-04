# Lists: An ordered structure containing any number of values
#
# 1. Lists in python don't have a specific data type
# 2. Lists in python don't have a specific size

'''
>>> x = [1, 2, 3]
>>> x
[1, 2, 3]
>>> y = [4, 5, 'Six', 7.89, False]
>>> y    
[4, 5, 'Six', 7.89, False]
>>> z = x + y
>>> z
[1, 2, 3, 4, 5, 'Six', 7.89, False]
'''


z = [1, 2, 3, 4, 5, 'Six', 7.89, False]
for i in z:
    print(i)


def print_list(message, l):
    print(message)

    for i in l:
        print(i)

    print('-----')


z.append(42)
print_list('Z after append:', z)

value = z.pop()
print('Popped value:', value)

print_list('Z after pop:', z)

# List indexing:
print(z[0])
print(z[3])
print(z[-1])  # To get last value
