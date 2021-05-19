#FINDING MEGA PRIME USING FUNCTION CALL.
import math
'''MEGA PRIME: A number 'n' is said to be mega prime,if 'n' is prime number as
   well as all the digits present in 'n' should be prime numbers.
   Eg:n=97
      Here,97 as well as 9 and 7 are prime.So 97 is mega prime.
'''

n=97
pc=0  #prime count
dc=0  #digit count
#Logic to check prime number.
def is_prime(n):
    x=int(math.sqrt(n))
    for i in range(2,x+1):
        if n%i==0:
            return False
        else:
            return True
if is_prime(n):
    while n:       #Logic to check each each number is prime.
        r=n%10
        n=n//10
        dc+=1
        if is_prime(r):
            pc+=1
    if pc==dc:
        print('mega prime')
    else:
        print('prime but not mega')
else:
    print('not prime')

#OR
#FINDING MEGA PRIME WITHOUT FUNCTION CALL.
'''
import math
n=97
pc=0
dc=0
x=int(math.sqrt(n))
for i in range(2,x+1):
    if n%i==0:
        #print('not prime')
        break
    else:
        #print('prime')
        while n:
            r=n%10
            n=n//10
            dc+=1
            y=int(math.sqrt(r))
            for i in range(2,y+1):
                if r%i==0:
                    #print('prime')
                    break
                else:
                    pc+=1
        if pc==dc:
            print('mega prime')
        else:
            print('prime but not mega prime')

 '''
