'''
arr=[-7,1,5,2,-4,3,0]
n=len(arr)
for i in range(1,n-1):
    ls=0
    rs=0
    for j in range(0,i):
        ls+=arr[j]
    for k in range(i+1,n):
        rs+=arr[k]
    if(ls==rs):
        print(i)
        break
'''

#OR


'''finding an index where sum of elements of its LHS is equal to sum of
elements of RHS.'''
arr=[-7,1,5,2,-4,3,0]    
n=len(arr)
prefix=[0 for i in range(len(arr))] #[-7,6,-1,1,-3,0,0]
prefix[0]=arr[0]
prefix.append(arr[0])
for i in range(1,len(arr)):
    prefix[i]=(prefix[i-1]+arr[i])
ls=0
rs=0
for i in range(1,len(arr)-1):
    ls=prefix[i-1]
    rs=prefix[n-1]-prefix[i]
    if(ls==rs):
        print(i)
        break
