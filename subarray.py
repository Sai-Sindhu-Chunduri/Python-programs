'''
arr=[2,4,5,6,7,11]
n=len(arr)
for i in range(n):
    for j in range(i,n):
        
        print(arr[i:j])
'''
n=int(input("Enter the number of array elements"))
arr=list(map(int,input("Enter n elements").split()))
q=int(input("Enter number of queries"))
for num in range(q):
    l,r=map(int,input("Enter the range").split())
    ssum=0
    for i in range(l,r+1):
        ssum=ssum+arr[i]
    print(ssum)
