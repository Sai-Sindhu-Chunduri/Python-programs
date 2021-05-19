'''Take a dictionary as input and print the key-value pairs which consists of
   a given suffix.'''

n=int(input())
d={}
suf=input()
for i in range(n):
    a=int(input())
    b=input()
    if b.endswith(suf):
        d[a]=b
print(d)


'''
for i in range(n):
    a=int(input())
    d[a]=input()
d1={key:val for key,val in d.items() if val.endswith(suf)}
print(d1) '''
    
