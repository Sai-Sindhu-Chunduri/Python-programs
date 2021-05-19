'''Take a dictionary as input and print the symmetric key value pairs.
   Example: {1:2,2:1,3:4,4:3}'''

n=int(input())
d={}
for i in range(n):
    a=int(input())
    d[a]=int(input())
temp={(x,y) for x,y in d.items()}
res={x:y for (x,y) in temp if (y,x) in temp}
print(res)

'''
INPUT:
3
1
2
2
1
3
2
OUTPUT:
{1: 2, 2: 1}
'''
