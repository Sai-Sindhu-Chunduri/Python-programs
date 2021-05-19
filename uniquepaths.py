'''A robot is located at the top-left corner of a m x n grid (marked 'Start' in
the diagram below).The robot can only move either down or right at any point
in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?
An image of 3 rows and 7 columns grid will be shown.
Start is at 1st row-1st column,end is at 3rd row last box-and-7th column last
box.
Example 1:
Input: m = 3, n = 7
Output: 28
'''

m=int(input())
n=int(input())
arr=[[0 for i in range(n)] for j in range(m)]
for i in range(m):
    for j in range(n):
        if i==0 or j==0:
            arr[i][j]=1
        else:
            arr[i][j]=arr[i-1][j]+arr[i][j-1]
print(arr[m-1][n-1])
