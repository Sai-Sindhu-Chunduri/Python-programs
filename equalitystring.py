'''Sanath is a well versed student in the college.A new principal came to
college and gets to know about the knowledge of sanath.He wants to test sanath
and he has given a task like this:Given a sentence he needs to determine whether
the sentence contains equal number of lowercase alphabets,uppercase alphabets,
digits,symbols,If so he needs to say "Equality For Everyone" otherwise he needs
to say :"No Equality",sanath wants to prove his ability to the new principal.
So help Sanath.'''

s=input()
l=0
u=0
d=0
ss=0
for i in s:
    if i.islower():
        l+=1
    if i.isupper():
        u+=1
    if i.isdigit():
        d+=1
    else:
        ss+=1
if(l==u==d==ss):
    print("Equality For Everyone")
else:
    print("No Equality")

'''Sample input:
   aB1$
   Sample output:
   Equality for Everyone

   Sample input2:
   ab23$%
   Sample output2:
   No Equality
'''
   
