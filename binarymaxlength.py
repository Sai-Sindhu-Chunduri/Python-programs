'''Given the number, find length of the longest consecutive 1's in binary
   representation.'''

def maxnum(array,n):
    count=0
    result=0
    for i in range(0,n):
        if (array[i]==0):
            count=0
        else:
            count+=1
            result=max(result,count)
    return result

m=int(input())
array=list(map(int,input().split()))
n=len(array)
print(maxnum(array,n))


