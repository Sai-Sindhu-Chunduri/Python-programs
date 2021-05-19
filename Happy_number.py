'''HAPPY NUMBER:A number is said to be happy when if it yields 1 when replaced
   by the sum of its digits repeatedly.
   Eg:number=130
     1**2+3**2+0**2=10
     1**2+0**2=1.
'''

n=130
sum=0
while True:
    r=n%10
    n=n//10
    sum=sum+r**2
    if n==0:
        n=sum
        sum=0
        if n>=1 and n<=9:
            break
if n==1:
    print('Happy Number')
else:
    print('Not happy number')




