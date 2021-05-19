#Take a tuple as input and create a dictionary with adjacent pairs in tuple.

n=int(input())
t=tuple(map(int,input().split()))[:n]
d={t[i]:t[i:i+2] for i in range(0,len(t),2)}
print(d)

'''
INPUT:
6
1 2 3 4 5 6
OUTPUT:
{1: (1, 2), 3: (3, 4), 5: (5, 6)}
'''


'''n=int(input())
t=tuple(map(int,input().split()))[:n]
d={t[i]:t[i:i+1] for i in range(0,len(t),2)}
print(d)
'''

'''
INPUT:
6
1 2 3 4 5 6
OUTPut:
{1: (1,), 3: (3,), 5: (5,)}
'''
