arr=[2,5,12,1,4,3,9]
arr.sort()
temp=25
flag=0
for i in range(len(arr)):
    j=i+1
    k=len(arr)-1
    s=temp-arr[i]
    while(j<k):
        if arr[j]+arr[k]==s:
            print(arr[i],arr[j],arr[k])
            flag=1
            break
        elif arr[i]+arr[j]>s:
            k-=1
        else:
            j+=1
if(temp==flag):
    print("found")
else:
    print('not found')
