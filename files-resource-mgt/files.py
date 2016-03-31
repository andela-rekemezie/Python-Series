import sys


def main(filename):
    result = open(filename, 'rt', encoding='utf-8')
    for line in result:
        sys.stdout.write(line)
    result.close()
if __name__ == '__main__':
    main(sys.argv[1])