#Take a dictionary as input and print the reversed order of keys as a list.

n=int(input())
d={}
for i in range(n):
    a=int(input())
    d[a]=int(input())
print(d.keys())
l=list(d.keys())
print(list(reversed(l)))

'''
INPUT:
3
1
2
3
4
5
6
OUTPUT:
dict_keys([1, 3, 5])
[5, 3, 1]
'''
