# implementation of comprehension with list
[len(str(factorial(x))) for x in range(30)]
[1, 1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18, 19, 20, 22, 23, 24, 26, 27, 29, 30, 31]
# implementation of comprehension with set
{len(str(factorial(x))) for x in range(30)}
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18, 19, 20, 22, 23, 24, 26, 27, 29, 30, 31}

# implementation of dictionary compprehension
>>> import os
>>> import glob
>>> from pprint import pprint as pp
>>> file_sizes = {os.path.realpath(p):os.stat(p).st_size for p in glob.glob('*.py')}
>>> pp(file_sizes)