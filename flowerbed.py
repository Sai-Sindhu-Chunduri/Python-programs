'''Suppose you have a long flowerbed in which some of the plots are planted
and some are not. However, flowers cannot be planted in adjacent plots - they
would compete for water and both would die.
Given a flowerbed (represented as an array containing 0 and 1, where 0 means
empty and 1 means not empty), and a number n, return if n new flowers can be
planted in it without violating the no-adjacent-flowers rule.
Example 1:
Input:
5
1 0 0 0 1
1
Output:
True
Example 2:
Input:
5
1 0 0 0 1   
2
Output: 
False
'''

import math
n=int(input())
l=list(map(int,input().split()))[:n]
m=int(input())
l1=l[0:n:1]   #l1=l[0:n:1]
suml1=sum(l1)
ans=True
res=math.ceil(n/2)
if((suml1+m)<=res):  #Or if((suml1+m)<=res and n!=2):
    print(ans)
else:
    ans=False
    print(ans)
