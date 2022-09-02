#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    """
    Convert AM/PM Time to military format
    """
    # Write your code here
    morning = True
    if s[-2:] == "PM":
        morning = False
    s = s[:-2]
    splitString = s.split(':')
    if morning:
        splitString[0] = "{:02d}".format(int(splitString[0]) % 12)
    else:
        splitString[0] = "{:02d}".format((int(splitString[0]) % 12) + 12)
    ans = ""
    for val in splitString:
        ans += str(val) + ":"
    return ans[:-1]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
