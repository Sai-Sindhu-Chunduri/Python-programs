#PATTERNS:
n=5
i=0
c=0
while 1:
    i+=1
    print(i,end=" ")
    if i==n:
        i=0
        c+=1
        print()
        if c==n:
            break

'''OUTPUT:
   1 2 3 4 5
   1 2 3 4 5
   1 2 3 4 5
   1 2 3 4 5
   1 2 3 4 5
'''
        
