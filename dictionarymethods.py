Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: C:\Python Challenges\sumindices.py =================
0 1
>>> d=dict([(1,2),(3,4)])
>>> d
{1: 2, 3: 4}
>>> d={}
>>> d
{}
>>> d={1:1,2:2,3:3}
>>> d
{1: 1, 2: 2, 3: 3}
>>> d=dict('name','sindhu')
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    d=dict('name','sindhu')
TypeError: dict expected at most 1 arguments, got 2
>>> d=dict(('name','sindhu'))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    d=dict(('name','sindhu'))
ValueError: dictionary update sequence element #0 has length 4; 2 is required
>>> d=dict([('name','sindhu')])
>>> d
{'name': 'sindhu'}
>>> d=dict([('name','sindhu'),(])
       
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> d={1:1,2:2,3:3,4:4,5:5}
>>> lena9d)
SyntaxError: invalid syntax
>>> len(d)
5
>>> 1 in d
True
>>> 6 not in d
True
>>> for i in d:
	print(d[i],end=" ")

	
1 2 3 4 5 
>>> d={1:6,2:7,3:8,4:9,5:5}
>>> d
{1: 6, 2: 7, 3: 8, 4: 9, 5: 5}
>>> for i in d:
	print(d[i],end=" ")

6 7 8 9 5 
>>> my_dict={'name':'sindhu','age':19}
>>> my_dict['name']
'sindhu'
>>> d.get(1)
6
>>> dir(dict)
['__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
>>> del d[3]
>>> d
{1: 6, 2: 7, 4: 9, 5: 5}
>>> d.clear()
>>> d
{}
>>> d={1:1,2:2,3:3,4:4,5:5}
>>> d1=d.copy()
>>> d
{1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
>>> d[6]=6
>>> d
{1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
>>> d1
{1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
>>> id(d)
2352554703432
>>> id(d1)
2352554665288
>>> d.fromkeys(d)
{1: None, 2: None, 3: None, 4: None, 5: None, 6: None}
>>> d.fromkeys(d,0)
{1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
>>>  d.fromkeys([1,2,3,4,5],0)
 
SyntaxError: unexpected indent
>>> d.fromkeys([1,2,3,4,5],0)
{1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
>>> d[1]=5
>>> d
{1: 5, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
>>> d.get(2)
2
>>> d.get(7)
>>> d.items()
dict_items([(1, 5), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6)])
>>> d.keys()
dict_keys([1, 2, 3, 4, 5, 6])
>>> d.values()
dict_values([5, 2, 3, 4, 5, 6])
>>> d.pop(1)
5
>>> d.pop(7)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    d.pop(7)
KeyError: 7
>>> d
{2: 2, 3: 3, 4: 4, 5: 5, 6: 6}
>>> d.popitem()
(6, 6)
>>> d
{2: 2, 3: 3, 4: 4, 5: 5}
>>> d.setdefault(2,0)
2
>>> d
{2: 2, 3: 3, 4: 4, 5: 5}
>>> d.update([(1,1),(6,6)])
>>> d
{2: 2, 3: 3, 4: 4, 5: 5, 1: 1, 6: 6}
>>> d.__contains__(1)
True
>>> d.__getitem__(2)
2
>>> d
{2: 2, 3: 3, 4: 4, 5: 5, 1: 1, 6: 6}
>>> d.__delitem__(2)
>>> d
{3: 3, 4: 4, 5: 5, 1: 1, 6: 6}
>>> 