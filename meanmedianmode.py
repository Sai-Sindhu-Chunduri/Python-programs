l=[1,2,3,4,5,6,7,8,9]
def mean(l):
   print(sum(l)/len(l))
def median(l):
    l.sort()
    n=len(l)
    if n%2==1:
        print(l[int((n-1)/2)])
    else:
        s=l[int((n-1)/2)]+l[int(n/2)]
    print(s/2)
def mode(l):
    p=dict((x,l.count(x)) for x in set(l))
    fl=sorted(p.items(),key=lambda x:x[1],reverse=True)
        #print(fl)
    ffl=max(fl,key=lambda x:x[1])
    print(ffl[0])
mean(l)
median(l)
mode(l)

'''
5.0
5
Traceback (most recent call last):
  File "C:/python programs/meanmedianmode.py", line 19, in <module>
    median(l)
  File "C:/python programs/meanmedianmode.py", line 11, in median
    print(s/2)
UnboundLocalError: local variable 's' referenced before assignment
'''
