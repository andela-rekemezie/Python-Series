# testing tuples using destructuring
def minmax(num):
    return min(num), max(num)

# Uncomment to call the function
# numbers = [9, 8, 4, 3]
# lower, higher = minmax(numbers)
# print(lower)
# print(higher)
#
# Tuples unpacking works arbitraily with nested tuples
# (a, (b, c, (d, e))) = (1, (2, 3, (4, 5)))
#
# Idiomatic python swap
# a = 'Rowland'
# b = 'Eby'
# a, b = b, a
# print(a) #  => Eby
#
# partition on str returns tuple
# 'unforgettable'.partition('forget')
# start, separator, destination = 'Sabo:Yaba'.partition(':')
#
