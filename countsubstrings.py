T=int(input("Enter number of testcases:"))
for i in range(T):
    N=int(input("Enter the length of the string:"))
    S=input("Enter the string")
    l=list(S)
    length=l.count('1')
    result=length*(length+1)//2
    print(result)
