#This program is to check whether given number is prime or not.
r=5
factor_count=0
for i in range(1,r+1):
    if r%i==0:
        factor_count+=1
if factor_count==2:
    print('Prime')
else:
    print('Not Prime')
