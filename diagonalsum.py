'''Given a square matrix mat, return the sum of the matrix diagonals.Only
include the sum of all the elements on the primary diagonal and all the
elements on the secondary diagonal that are not part of the primary diagonal.
Example 1:
Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
'''

mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
n=len(mat)
pd=sd=0
for i in range(n):
    for j in range(n):
        if i==j:
            pd+=mat[i][j]
        elif i+j==n-1:
            sd+=mat[i][j]
print(pd+sd)

#OR
'''
mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]
n=len(mat)
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print(mat[i][j])
'''
