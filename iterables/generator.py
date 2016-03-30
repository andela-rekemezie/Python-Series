def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item

# the count funciton
def run_take():
    items = ['great', 'Python', 'Java', 'Ruby']
    for item in take(3, items):
        print(item)

def distint(num):
    seen = set()
    for item in num:
        if item in seen:
            continue
        yield (item)
        seen.add(item)

def run_distinct():
    items =  [4, 6, 8, 2, 4, 5, 6,8, 4]
    for item in distint(items):
        print(item)

def run_pipeline():
    print ('This is the generator pipleline')
    items = [9, 3, 5, 2, 4]
    for item in take(3, distint(items)):
        print (item)

if __name__ == '__main__':
    run_take()
    run_distinct()
    run_pipeline()

