n=int(input())
arr=list(map(int,input().split()))
arr.insert(0,0)
stack=[]
stack.append(0)
count=0
for i in range(1,len(arr)):
    if(arr[i]>0):
        stack.append(i)
        continue
    if(arr[stack[-1]]==-1*arr[i]):
        stack.pop()
        count=max(count,i-stack[-1])
    else:
        stack.append(i)
print(count)


'''OUTPUT:
   4
   1 2 -2 -1
   2
'''
