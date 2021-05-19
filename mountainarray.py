#arr=[1,2]
arr=[3,5,3]
x=sorted(arr)
if arr==x or arr==x[::-1]:
    print('false')
elif len(arr)<=2:
    print('false')
else:
    arr.append(-1)
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            arr[i]=0
        elif arr[i]>arr[i+1]:
            arr[i]=1
        else:
            print('false')
            break
    del arr[-1]








'''arr=[0,2,3,4,5,2,1,0]
x=arr.index(max(arr))
if arr[x]>arr[x-1] and arr[x]>arr[x+1]:
    arr1=arr[0:x]
    arr2=arr[x+1:]
    if len(arr1)==1:
        s1=1
    else:
        for i in range(len(arr1)):
            if arr[i]<arr[i+1]:
                s1=1
            else:
                s1=0
                break
    if len(arr1)==1:
        s2=1
    else:
        for j in range(len(arr2)-1):
            if arr2[j]>arr2[j+1]:
                s2=1
            else:
                s2=0
                break
    if s1==1 and s2==1:
        print('true')
            
else:
    print('false')'''
