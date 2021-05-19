'''Given a string,compute recursively(no loops) the number of lower case 'x'
   chars in string.
   Example:
   countX("axxhixxbc") --> 4
'''

def countX(s):
    if len(s)=-0:
        return 0
    elif s[0]=='x':
        return 1+countX(s[1:])
    else:
        return countX(s[1:])
