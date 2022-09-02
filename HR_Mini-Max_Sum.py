#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    #sort array and slice front part and back part of array
    arr = sorted(arr)
    sum1 = sum(arr[:-1])
    sum2 = sum(arr[1:])
    #print results to output
    print(sum1,sum2)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
