'''Take two dictionaries as inut and print a new dictionary which consists
   of product of the given input dictionaries.
   NOTE:Keys should be same.'''

n=int(input())
d={}
d1={}
d2={}
for i in range(n):
    a=input()
    d[a]=int(input())
    d1[a]=int(input())
    d2[a]=d1[a]*d[a]
print(d)
print(d1)
print(d2)

#d2={key:d1[key]*d[key] for key in d1}  --> dictionary comprehensions.
