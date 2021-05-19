'''Program to print the sum of all the elements,except element in the given
   index,element before and after the given index number from the given list.'''

n=int(input())              
l=[]           
for i in range(n):          
    l.append(int(input()))  
ind=l.index(num)            
l1=l[:ind-1]+l[ind+2:]  
print(sum(l1))   
 
