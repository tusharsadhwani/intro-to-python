# Python is a High Level Programming language
# It takes away most of the logic burden from the user

# For eg. Fibonacci sequance

# Output:
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34

''' C++:

#include <bits/stdc++.h>
using namespace std;

int main() {
    int i = 1, j = 1, temp;
    while (i < 50) {
        cout << i << endl;
        temp = j;
        j += i;
        i = temp;
    }
    return 0;
}

'''

# Python:

i, j = 1, 1
while (i < 50):
    print(i)
    i, j = j, i+j
