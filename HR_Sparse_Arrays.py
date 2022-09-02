#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
#

def matchingStrings(strings, queries):
    """
    There is a collection of input strings and a collection of query strings.
    For each query string, determine how many times it occurs in the list of input strings.
    Return an array of the results.
    """
    # Write your code here
    #create a dictionary and iterate through array. Keep track of occurances in dictionary
    #iterate through queries and append queries to dictionary to answer array.
    occurances = dict()
    ans = []
    for string in strings:
        occurances[string] = 1 + occurances.get(string,0)
    for query in queries:
        ans.append(occurances.get(query,0))
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    strings_count = int(input().strip())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
