# print 1 2 3 4 5 4 3 2 1(depends on n).
# method only using one loop.
n=5
i=1
s=True
while i:
    if s==True:
        print(i,end=" ")
        i+=1
    if i==n:
        s=False
    if s==False:
        print(i,end=" ")
        i-=1


#Method using 2 loops.
'''n=6
for i in range(1,n+1):
    print(i,end=" ")
for j in range(n-1,0,-1):
    print(j,end=" ")'''

#or
'''n=6
i=1
while n:
    if i<=n-1:
        print(i,end=" ")
        i+=1
    else:
        print(n,end=" ")
        n-=1'''
#or
#Method using function.
'''def series(n,i=1):
    i=1
    while n:
        if i<=n-1:
            print(i,end=" ")
            i+=1
        else:
            print(n,end=" ")
            n-=1
series(6)
'''    
        
    
    
    
