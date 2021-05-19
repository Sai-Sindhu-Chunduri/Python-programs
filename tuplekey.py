n=int(input())
d={}
l=[list(input().split()) for i in range(n)]
print(l)
for i in l:
    if len(i[0])>1:
        d[tuple(map(int,i[0].split(',')))]=int(i[1])
    else:
        d[int(i[0])]=int(i[1])
print(d)
for k in d.keys():
    if type(k)==tuple:
        print(d[k])

'''
INPUT:
3
1,2,3 3
3 4
4 5
OUTPUT:
[['1,2,3', '3'], ['3', '4'], ['4', '5']]
{(1, 2, 3): 3, 3: 4, 4: 5}
3
'''

        
