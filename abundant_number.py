'''The abundant number can be called as an excessive number and defined as the
   number for which the sum of its proper divisors is greater than the number
   itself.A first abundant number is the integer 12 having the sum (16) of its
   proper divisors (1, 2, 3, 4, 6) which is greater than itself (12).
   Examples: 12, 18, 20, 24, 30, 36'''

'''import math
n=int(input("Enter a number: "))
temp=n
fact=0
sum=0
for i in range(1,n+1):
    if n%i==0:
        fact=fact+i
    sum+=fact
if(sum>temp):
    print('Abundant number')
else:
    print('Not abundant number')'''

import math
def getsum(n):
    sum=0
    i=1
    while i<=(math.sqrt(n)):
        if n%i==0:
            if n/i==i:
                sum=sum+i
            else:
                sum=sum+i
                sum=sum+(n/i)
        i=i+1
    sum=sum-n
    return sum
def abundant(n):
    if(getsum(n)>n):
        return 1
    else:
        return 0
if(abundant(12)==1):
    print("Abundant number")
else:
    print("Not abundant number")
              
