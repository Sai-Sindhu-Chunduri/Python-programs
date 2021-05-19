import math
def is_prime(n):
    x=int(math.sqrt(n))
    for i in range(2,x+1):
        if n%i==0:
            return False
        else:
            return True
def position_prime(n):
    if n==2:
        return 1
    if is_prime(n):
        return 1+position_prime(n-1)
    return 0+position_prime(n-1)
if is_prime(2):
    if is_prime(position_prime(2)):
        print('super prime')
    else:
        print('not super prime')
else:
    print('not a prime')




# prime number: 2 3 5 7 11
# position    : 1 2 3 4 5  
        
