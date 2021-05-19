'''SUPER PRIME is a number where the number as well as the position of digits of
 the number should also sbe prime
# prime number: 2 3 5 7 11
# position    : 1 2 3 4 5  '''
import math
n=11
def is_prime(n):
    x=int(math.sqrt(n))
    for i in range(2,x+1):
        if n%i==0:
            return False
        else:
            return True
    def position_prime(n):
        position=0
        for i in range(1,n+1):
            if is_prime(i):
               position+=1
        return position
    if is_prime(11):
        if is_prime(position_prime(11)):
            print('super prime')
        else:
            print('not super prime')
    else:
        print('not a prime')





