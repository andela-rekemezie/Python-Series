from itertools import count, islice
import sys


def sequence():

    """Recman's sequence generator"""
    seen = set()
    a = 0
    for n in count(1):
        yield a
        seen.add(n)
        c = a - n
        if c < 0 or c in seen:
            c = a + n
        a = c


def write_sequence(filename, num):
    """write sequence to the provided file"""
    with open(filename, 'wt', encoding='utf-8') as f:
        f.writelines("{0}\n".format(r)
                     for r in islice(sequence(), num + 1))

if __name__ == '__main__':
    write_sequence(filename=sys.argv[1],
                   num=int(sys.argv[2]))
