from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        You are given an integer array nums.
        You are initially positioned at the array's first index,
        and each element in the array represents your maximum jump
        length at that position.

        Return true if you can reach the last index,
        or false otherwise.
        """
        #need to work backwards. Greedy algorithm to find
        #which index has a value that can reach "needed index"
        #set first index to next to last length
        i = len(nums) -2
        #set needed index to last index initially
        neededIndex = len(nums)-1
        #while i >= 0, update needed index
        while i >= 0:
            #if current index can jump to needed index, set neededindex to current index
            if nums[i] + i >= neededIndex:
                neededIndex = i
            #decrease i by 1
            i -= 1
        #if needed index is 0 (has made it all the way backwards through array, return True)
        if neededIndex == 0:
            return True
        #otherwise return false
        return False