#Program to give vowel count.
s=input()
a="aeiouAEIOU"
count=0
'''for i in s:
    if i in a:
        count+=1
print("count of vowels is ",count)'''

#or --> Wroking with range:
for i in range(len(s)):
    if s[i] in a:
        count+=1
print("count of vowels is ",count)
    
