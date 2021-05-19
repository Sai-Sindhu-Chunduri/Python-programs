n=int(input("Enter the number of array elements"))
arr=list(map(int,input("Enter array elements").split()))
prefix=[0 for i in range(len(arr))]   
for i in range(0,n-1):
    prefix[i]=prefix[i-1]+arr[i]
for i in range(0,len(arr)-1):
    ls=0
    rs=0
    ls=prefix[i-1]
    rs=prefix[n-1]-prefix[i]
    if(ls==rs):
        print(i)
        

#-7,1,5,2,-4,3,0
