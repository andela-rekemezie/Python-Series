def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == item:
            return
        counter += 1
        yield item

# the count funciton
def run_take():
    items = ['great', 'Python', 'Java', 'Ruby']
    for item in take(3, items):
        print(item)

if __name__ == '__main__':
    run_take()
    run_distinct()

def distint