'''HARSHAD NUMBER:If a number is divisible by the sum of its digits,
   then it will be known as a Harshad Number.
   For example:
   The number 156 is divisible by the sum (12) of its digits (1, 5, 6 ).
'''

n=156
temp=n
sum=0
while n:
    r=n%10
    n=n//10
    sum+=r
    if n==0:
        break
if temp%sum==0:
       print('Harshad Number')
else:
    print('Not Harshad Number')
        
