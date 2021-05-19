N=7
A=[3,7,5,6,6,5,5]
A.sort()
sumA=sum(A)
h=sumA//2
count=0
bobsum=0
for i in range(len(A)-1,-1,-1):
    bobsum=bobsum+A[i]
    count+=1
    if(bobsum>h):
        break
print(count)
    
    
