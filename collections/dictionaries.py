from pprint import pprint as pp
# dict construct can be used to covert a tuple into a dictionry
num = [('Jone', 5), ('Doe', 56), ('Maya', 53)]
x = dict(num)
print(x)

vowels = dict(a='animal', o='onions', e='elephant', u='union', i='iterables')
print(vowels)

# using the update method to update a dictionary
x.update(vowels)
print(pp(x))