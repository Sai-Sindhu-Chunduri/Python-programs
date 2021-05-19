'''Given a string as input,you need to reverse the string without reversing the
letters in it.
Example: Input:"Aditya Engineering College"
         Output:'College Engineering Aditya'
'''
s=input()
rev=" ".join(reversed(s.split()))
print(rev)
