n=5
z=1
for i in range(1,n+1):
    for sp in range(n-1,i-1,-1):
        print(' ',end="")
    for j in range(1,z+1):
        print("*",end="")
    print()
    z+=2

'''OUTPUT:
       *
      ***
     *****
    *******
   *********
'''
