#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    #keeps counters of plus, minus and zero vals
    pos = 0
    neg = 0
    zero = 0
    for val in arr:
        if int(val) > 0:
            pos += 1
        elif int(val) < 0:
            neg += 1
        else:
            zero+= 1
    #prints formatted values to output
    print("{ratio: .6f}".format(ratio=float((pos/len(arr)))))
    print("{ratio: .6f}".format(ratio=float((neg/len(arr)))))
    print("{ratio: .6f}".format(ratio=float((zero/len(arr)))))
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
