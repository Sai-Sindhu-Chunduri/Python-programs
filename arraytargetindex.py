'''Program to print the starting and ending index of the given element from the
   given array.If the element is not present,then print [-1,-1]'''


def occurences(nums,val):
    if val not in nums:
        print(-1,end=" ")
        print(-1)
    else:
        for i in range(0,len(nums),1):
            if nums[i]==val:
                print(i,end=" ")
                break
        for i in range(len(nums)-1,0,-1):
            if nums[i]==val:
                print(i)
                break
n=int(input())
nums=list(map(int,input().split()))
val=int(input())
occurences(nums,val)

'''
INPUT:
6
5 7 7 8 8 10
8
OUTPUT:
3 4
'''


















