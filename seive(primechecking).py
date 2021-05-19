x=int(input("Enter a number to check"))
n=25
seive=[1 for i in range(n+1)]
seive[0]=0
seive[1]=0
for i in range(2,int(n**0.5)+1):
    if seive[i]==1:
        for j in range(i*i,n,i):
            seive[j]=0
if seive[x]==1:
    print("Prime")
else:
    print("Not a prime")


