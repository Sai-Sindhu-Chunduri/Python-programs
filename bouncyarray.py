arr=[2,5,3,6,4,8,7]
us=0
ds=0
if arr[0]>arr[1]:
    ds=1
if arr[0]<arr[1]:
    us=1
for i in range(1,len(arr)-1):
    if us==1:
        if arr[i]>arr[i+1]:
            ds=1
            us=0
        else:
           print('Not bouncy')
           break
    else:
        if ds==1:
            if arr[i]<arr[i+1]:
                us=1
                ds=0
            else:
                print('Not bouncy')
                break
else:
    print('Bouncy array')
