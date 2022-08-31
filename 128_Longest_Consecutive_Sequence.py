from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Given an unsorted array of integers nums,
        return the length of the longest consecutive elements sequence.

        You must write an algorithm that runs in O(n) time.
        """
        #create a set of the nums array (remove duplicates)
        setNums = set(nums)
        #set return val to 0 (total number of consecutive elements)
        returnVal = 0
        #iterate through array O(n)
        for val in nums:
            #if val-1 is not in setNums (lower value exists)
            if val-1 not in setNums:
                #set y to next value in consecutive sequence
                y = val + 1
                #while next value is in the set, increase y
                while y in setNums:
                    y+=1
                #take max of current return val and longest consecutive sequence minus start
                returnVal = max(returnVal,y-val)
        #return max consecutive elements
        return returnVal