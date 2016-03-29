def gen345():
    print('about to render 3')
    yield 3
    print('about to render 4')
    yield 4
    print('about to render 5')
    yield 5

h = gen345()
next(h)
about to render 3
3
next(h)
about to render 4
4
next(h)
about to render 5
5
next(h)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

for i in gen345():
    print(i)
