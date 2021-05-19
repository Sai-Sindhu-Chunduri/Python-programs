'''There is a prison where everyday a new password is generated to lock the
prisoners.The password is related to time of the day and the secret
series denoted as:
An=(2*(An-1))-1
The hour in current time tells the first term(A0) in the series
The minute in current time tells the number of repetitions to be performed to
generate the series of elements.
Example:
Let's sat the time as23:05 then A0=23 and no of repetitions=5,then series
is generated as:
A0=23
A1=2*23-1=45
A2=2*45-1=89
A3=2*89-1=177
A4=2*177-1=353
A5=2*353-1=705
Then we add all termsobtained in each repitition including first term
23+45+89+177+353+705=1392
After getting the result,we will generate the password for lock as follows:
1=B
3=D
9=J
2=C
So the password is BDJC
'''

import string
up=string.ascii_uppercase
h,m=map(int,input().split(':'))
s=h
for i in range(m):
    h=2*h-1
    s+=h
password=""
for i in str(s):
    password+=up[int(i)]
print(password)
