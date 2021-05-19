'''Given an array A of non-negative integers,return an array consisting of all
   the even elements of A,followed by all the odd elements of A.
   Sample Input:
   4
   3 1 2 4
   Sample Output:
   2 4 3 1
'''

n=4
arr=[3,1,4,2]
arr1=[]
arr2=[]
for i in range(n):
    if arr[i]%2==0:
        arr1.append(arr[i])
    else:
        arr2.append(arr[i])
print(arr1+arr2)


#OR
'''
n=4
arr=[3,1,4,2]
arr1=[x for x in arr if x%2==0]
arr2=[x for x in arr if x%2!=0]
print(arr1+arr2)

'''
