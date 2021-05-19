l=[]
n=int(input())
for i in range(n):
    l.append(input())
l[0]=int(l[0])
l[1]=int(l[1])
l[3]=float(l[3])
l[4]=bool(l[4])
print(l)
