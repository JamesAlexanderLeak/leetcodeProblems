import collections
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str])-> List[List[str]]:
        """
        Given an array of strings strs, group the anagrams together. You can
        return the answer in any given order.
        """
        #create a default dict for the answer
        ans = collections.defaultdict(list)
        #for string in input
        for s in strs:
            #create array of alphabet
            count = [0] * 26
            #for each letter in string, add value to index in alphabet
            for c in s:
                count[ord(c) - ord('a')] += 1
            #cast count as tuple and use as key
            #append string to list dictionary value
            ans[tuple(count)].append(s)
        #return anser values (lists)
        return ans.values()