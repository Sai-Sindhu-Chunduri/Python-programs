#Take a dictionary as input and check whether a tuple exists as a key.

'''d={(1,2,3):1,"name":"IT"}
for k in d.keys():
    if type(k)==tuple:
        print(d[k])'''

n=int(input())
d={}
for i in range(n):
    a=tuple(map(int,input().split()))
    d[a]=int(input())
print(d)        

                   
    
