'''Take a string as input.The string consists of a character succeeded by a
number.Now you need to generate a new string as output in such a way that it is
formed by repeating each character for the number of times it is succeeded by
the given number. '''

s=input()
s1=""
for i in s:
    if i.isalpha():
        s1+=i
        x=i
    else:
        d=int(i)
        ns=x*(d-1)
        s1+=ns
print(s1)

'''sample input:
   a4b3c2
   sample output:
   aaaabbbcc
'''
