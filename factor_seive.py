
n=100
seive=[i for i in range(n+1)]
for i in range(2,int(n**0.5)+1):
    if seive[i]==i:
        for j in range(i*i,n+1,i):
            if seive[j]==j:
                seive[j]=i
x=int(input("Enter a number for getting factors":))
while(x!=1):
    print(seive[x])
    x=x//seive[x]
