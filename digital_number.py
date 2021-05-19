'''import math
#n=38
def digital_root(n):
    #Base case for recursion.
    if(len(str(n)))==1:
        return n
    #Get sum of number by turning it into string and looping through it.
    #adding each digit one by one.
    sum=0
    for i in range(n):
        sum+=int(i)
    #get the digital root of sum
    return digital_root(sum)
#n=38
print(digital_root(38))'''

'''import math
def digital_root(n):
    if(n==0):
        return 0
    if(n%9==0):
        return 9
    else:
        return n%9
digital_root(38)'''


def converttostring(sum):
    str1=""
    while(sum):
        str1=str1+chr((sum%10))+ord('0')
        sum=sum//10
    return str
def getindividualdigitsum(str1,len1):
    sum=0
    for i in range(len1):
        sum=sum+ord(str1[i])-ord('0')
    return converttostring(sum)
def getdigitalroot(str1):
    if(len(str1)==1):
        return ord(str[0])-ord('0')
    return getdigitalroot(str1)
if __name__=='__main__':
    str1="38"
    print(getdigitalroot(str1))
    
    
        
    
    
