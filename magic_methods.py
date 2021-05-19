Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,3,4,5]
>>> l.__add__([6,7,8,9,10])
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> dir(list)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> l.__contains__(6)
False
>>> l
[1, 2, 3, 4, 5]
>>> l.__contains__(5)
True
>>> l.__delitem__(1)
>>> l
[1, 3, 4, 5]
>>> l.__dir__()
['__repr__', '__hash__', '__getattribute__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__iter__', '__init__', '__len__', '__getitem__', '__setitem__', '__delitem__', '__add__', '__mul__', '__rmul__', '__contains__', '__iadd__', '__imul__', '__new__', '__reversed__', '__sizeof__', 'clear', 'copy', 'append', 'insert', 'extend', 'pop', 'remove', 'index', 'count', 'reverse', 'sort', '__doc__', '__str__', '__setattr__', '__delattr__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__dir__', '__class__']
>>> l=[1,2,3,4,5]
>>> l1=[1,2,3,4,5]
>>> l.__eq__(l1)
True
>>> l.__ne__(l1)
False
>>> l.__ge__(l1)
True
>>> l.__gt__(l1)
False
>>> l.__lt__(l1)
False
>>> l.__getitem__(1)
2
>>> l.__iadd__([6,7,8,9,10])
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> l
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> l1.__mul__(2)
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> l1
[1, 2, 3, 4, 5]
>>> l1.__imul__(2)
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> l1
[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
>>> l.__rmul__(2)
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> l=[1,2,3,4]
>>> l.__rmul__(2)
[1, 2, 3, 4, 1, 2, 3, 4]
>>> l.__iter__()
<list_iterator object at 0x00000265E9B831C8>
>>> l.__reversed__()
<list_reverseiterator object at 0x00000265E998A988>
>>> list(l.__reversed__())
[4, 3, 2, 1]
>>> l.__setitem__(3,5)
>>> l
[1, 2, 3, 5]
>>> l.__sizeof__()
72
>>> l.__str__()
'[1, 2, 3, 5]'
>>> l[0].__str__()
'1'
>>> 