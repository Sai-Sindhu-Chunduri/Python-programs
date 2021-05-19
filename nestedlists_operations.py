Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[["M.Rajababu","Associate Professor","HOD"],["K.Arun Bhaskar","Associate Professor","faculty"]]
>>> l[0][0]
'M.Rajababu'
>>> L=["Aditya",["Mech","ECE","EEE",["CSE","IT"]]]
>>> L[1]
['Mech', 'ECE', 'EEE', ['CSE', 'IT']]
>>> L[1][0]
'Mech'
>>> L[1][2]
'EEE'
>>> L[1][3][1]
'IT'
>>> l[-1][-3]
'K.Arun Bhaskar'
>>> L[-3]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    L[-3]
IndexError: list index out of range
>>> L[-1][-3]
'ECE'
>>> L[-1][-4]
'Mech'
>>> L[-1][-1][-1]
'IT'
>>> l[1][0]="B.Vinay Kumar"
>>> l
[['M.Rajababu', 'Associate Professor', 'HOD'], ['B.Vinay Kumar', 'Associate Professor', 'faculty']]
>>> l[-1][-3]="S.Neelima"
>>> l
[['M.Rajababu', 'Associate Professor', 'HOD'], ['S.Neelima', 'Associate Professor', 'faculty']]
>>> L[1][3][0]="AI"
>>> L
['Aditya', ['Mech', 'ECE', 'EEE', ['AI', 'IT']]]
>>> L[-1][-1][-2]="CSE"
>>> L
['Aditya', ['Mech', 'ECE', 'EEE', ['CSE', 'IT']]]
>>> L[1][3].append("AI")
>>> L
['Aditya', ['Mech', 'ECE', 'EEE', ['CSE', 'IT', 'AI']]]
>>> L[1].insert(3,["CIVIL","PT","AGRI","MINING"])
>>> L
['Aditya', ['Mech', 'ECE', 'EEE', ['CIVIL', 'PT', 'AGRI', 'MINING'], ['CSE', 'IT', 'AI']]]
>>> L[1][3].extend(["AE"])
>>> L
['Aditya', ['Mech', 'ECE', 'EEE', ['CIVIL', 'PT', 'AGRI', 'MINING', 'AE'], ['CSE', 'IT', 'AI']]]
>>> L[1][3][5]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    L[1][3][5]
IndexError: list index out of range
>>> L[1][3].pop()
'AE'
>>> L
['Aditya', ['Mech', 'ECE', 'EEE', ['CIVIL', 'PT', 'AGRI', 'MINING'], ['CSE', 'IT', 'AI']]]
>>> L[1][3]
['CIVIL', 'PT', 'AGRI', 'MINING']
>>> L[1].pop(3)
['CIVIL', 'PT', 'AGRI', 'MINING']
>>> L
['Aditya', ['Mech', 'ECE', 'EEE', ['CSE', 'IT', 'AI']]]
>>> L[1][2].pop(3)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    L[1][2].pop(3)
AttributeError: 'str' object has no attribute 'pop'
>>> 
>>> L[1][2].pop()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    L[1][2].pop()
AttributeError: 'str' object has no attribute 'pop'
>>> L[1][3].remove("AI")
>>> L
['Aditya', ['Mech', 'ECE', 'EEE', ['CSE', 'IT']]]
>>> del L[1][3][0]
>>> L
['Aditya', ['Mech', 'ECE', 'EEE', ['IT']]]
>>> len(L)
2
>>> len(L[1])
4
>>> len(L[1][3])
1
>>> for i inL
SyntaxError: invalid syntax
>>> for i in L:
	print(i)

	
Aditya
['Mech', 'ECE', 'EEE', ['IT']]
>>> 