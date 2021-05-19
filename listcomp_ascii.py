'''Prints ascii values from given string using list comprehension. '''

'''given_list=[input()]
result=[ord(y) for x in given_list for y in x] 
print(str(result))

#Here x refers to element in given_list and y refers to element in x.
'''

l=input()
result=[ord(x) for x in l]
print(result)
