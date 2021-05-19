'''Create a list of dictionaries as input and generate a new dictionary which
   consists of key value pairs in which the values mapped with keys in each
   dictionary to form a new key-value pair.
   INPUT:
   [{jagadeesh':771},{'rakesh':1234},{'jagadeesh':123}]
   OUTPUT:
   {'jagadeesh':[771,123],'rakesh':[1234]}
'''

n=int(input())
l=[]
for i in range(n):
    d={}
    a=input()
    d[a]=int(input())
    l.append(d)
print(l)
res={}
for i in l:
    for k,v in i.items():
        res.setdefault(k,[]).append(v)
print(res)
