#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#Given an array of integers, where all elements but one occur twice, find the unique element.

def lonelyinteger(a):
    """
    Given an array of integers,
    where all elements but one occur twice,
    find the unique element.
    """
    # Write your code here
    for i in a:
        #finds value of a where count == 1
        if a.count(i) == 1:
            return i
    #if .count cannot be used, another solution would be
    #to iterate through array, add value to "result" set
    #once found again, remove value from set. At end, return only
    #remaining value from set.
    #use set to make lookup of values O(1).

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
