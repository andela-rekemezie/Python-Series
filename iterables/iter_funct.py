from itertools import count, islice


def is_prime(n):
    if n < 2:
        return False
    count = 2
    while count < n - 1:
        if n % count == 0:
            return False
        count += 1
    return True

# using itertools generator functions to return an iterator
# that returns all selected items of the iterator object
fifty_prime = islice((x for x in count() if is_prime(x)), 50)
sum_fifty_prime = sum(islice((x for x in count() if is_prime(x)), 50))
print (list(fifty_prime))
print(sum_fifty_prime)

print (any(fifty_prime))
print (all(fifty_prime))
print (any(is_prime(x) for x in range(456, 890)))
print (all(name == name.title() for name in ['Osmond', 'Great', 'cupa']))

monday = [45, 53, 35, 234, 24]
tuesday = [43, 23, 43, 23, 12]

# zip returns tuple
for item in zip(monday, tuesday):
    print(item)
# Using tuple and packing
for mon, tues in zip(monday, tuesday):
    print ('Average = ', (mon + tues)/2)
# implementing min, max, and sum in zip
for day in zip(monday, tuesday):
    print ('Min = {:.4f}, Max = {:.4f} Ave = {:.3f}'.format(min(day), max(day), sum(day) / len(day)) )