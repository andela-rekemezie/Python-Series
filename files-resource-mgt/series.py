import sys


def read_series(filename):
    """sequence reader"""
    with open(filename, 'rt', encoding='utf-8') as f:
        return [int(line.strip()) for line in f]

def main(filename):
    """The calling method"""
    result = read_series(filename)
    print(result)

if __name__ == '__main__':
    main(sys.argv[1])
