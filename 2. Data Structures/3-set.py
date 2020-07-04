# Set: Set of unordered unique values
#
# Like a dictionary, but only the keys
# - Useful when you want a list of unique items, or
#   when you want to check if something is in a list or not

'''
>>> a = set()
>>> a
set()
>>> a.add(42)
>>> a
{42}
>>> a.add(5)
>>> a
{42, 5}
>>> primes = {2, 3, 5, 7, 11, 13, 15, 19}
>>> primes
{2, 3, 5, 7, 11, 13, 15, 19}
>>> primes.add(17)
>>> primes.remove(15)
>>> primes
{2, 3, 5, 7, 11, 13, 17, 19}
>>> primes.add(2)
>>> primes
{2, 3, 5, 7, 11, 13, 17, 19}
'''

primes = {2, 3, 5, 7, 11, 13, 17, 19}

print('Primes upto 20:')
for i in primes:
    print(i)

print()

print('Is 17 a prime?')
print(17 in primes)


print('Is 9 a prime?', 9 in primes)
