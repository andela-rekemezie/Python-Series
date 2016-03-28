>>> class1 = {'ab', 'bukky', 'jmoke', 'sanni'}
>>> class2 = {'great', 'chibz', 'lade', 'abimbola', 'amaka'}
>>> class3 = {'ab', 'great', 'goodness'}
>>> class1.issubset(class2)
False

>>> class1.isdisjoint(class2)
True

>>> class1.difference(class2)
{'sanni', 'jmoke', 'bukky', 'ab'}

>>> class1.difference(class3)
{'sanni', 'jmoke', 'bukky'}

>>> class1.intersection(class3)
{'ab'}
>>> class1.symmetric_difference(class3)
{'sanni', 'jmoke', 'goodness', 'great', 'bukky'}
>>> class1.union(class3)
{'sanni', 'jmoke', 'goodness', 'ab', 'bukky', 'great'}
>>> class3.issubset(class1)
False
>>> class4 = {'ab', 'bukky'}
>>> class4.issubset(class1)
True
>>> class1.issuperset(class4)
True
>>>