from typing import List
class Solution:
    def twoSum(self, nums: List[int],target: int) -> List[int]:
        """
        Given an array of integers nums and an integer taget,
        return two indices of the two numbers such that they add
        up to the target. You may assume that each input would have
        exactly one solution, and you may not use the same element
        twice.
        """
        #create a dictionary to store differences
        diction = dict()
        #iterate through nums
        for index,value in enumerate(nums):
            #subtract the target from the current value
            diff = target - value
            #if the difference is in the dicitonary, return index of the difference and cur index
            if diff in diction:
                return [diction[diff],index]
            #else, store key:value value:index
            else:
                diction[value] = index
