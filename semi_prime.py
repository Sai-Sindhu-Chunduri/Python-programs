#A semiprime is a natural number that is a product of two prime numbers.
#example: 2*3=6.

import math
def is_prime(n):
    x=int(math.sqrt(n))
    for i in range(2,x+1):
        if n%i==0:
            return False
    else:
        return True
n=91
x=int(math.sqrt(n))
for i in range(2,x+1):
    if is_prime(i):
        if n%i==0:
            n=n//i
            if is_prime(n):
                print('semi prime')
                break
else:
    print('not a semi prime')



