arr=[1,2,4,5,6,8]
i=0
j=0
target=9
s=0
while(j<=len(arr)-1):
    if(s<target):
        s+=arr[j]
        j+=1
        print(s)
        
    elif(s>target):
        i+=1
        s-=arr[i]
        print(s)
    else:
        if arr[i]==arr[j]:
            print(arr[i])
        
        
