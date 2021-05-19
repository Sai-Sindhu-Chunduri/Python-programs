#A strong number is a number that is equal to the sum of factorial of its digits.

n=145
sum=0
temp=n
while n:
    r=n%10                      
    n=n//10
    fact=1
    for i in range(1,r+1):   #Logic for finding factorial.
        fact=fact*i             
    sum=sum+fact             #sum of factorial of digits.  
if(sum==temp):
    print('strong number')
else:
    print('not Strong number')
    
