arr=[4,3,12,1,1,1,10,6]
stack=[]
target=[0]*len(arr)
target[-1]=-1
stack.append(arr[-1])
for i in range(len(arr)-2,-1,-1):
    #print(arr[i])
    while stack!=[] and arr[i]>=stack[-1]:
        stack.pop()
    if stack==[]:
        target[i]=-1
    else:
        target[i]=stack[-1]
    stack.append(arr[i])
print(target)


'''
OUTPUT:
[12, 12, -1, 10, 10, 10, -1, -1]
'''
