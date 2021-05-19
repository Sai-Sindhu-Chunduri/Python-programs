'''Print vowels from given string using list comprehension.'''
string=input()
vowels="AEIOUaeiou"
s=[x for x in string if x in vowels]
print(s)
