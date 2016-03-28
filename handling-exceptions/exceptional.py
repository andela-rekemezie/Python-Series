'''A module for demonstrating exception handling '''
import sys
from math import log
def convert(s):
    try:
        return int(s)
    except (TypeError, ValueError) as e:
        print("Something went wrong: {}".format(str(e)), file=sys.stderr)
        print('conversion failed')
        raise # return -1 couls be used here but since another function call
              # call this, it's crucial to raise the exception againfor more error desciption
def sring_log(s):
    x = convert(s)
    return log(x)