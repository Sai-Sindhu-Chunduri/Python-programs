base,exp=map(int,input("Enter base and exponent:").split())
ans=base
while(exp!=1):
    if(exp%2==0):
        ans=ans*base
        base=base*base
        exp=exp/2
    else:
        ans=ans*base
        exp=exp-1
print(ans)
