from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Given an integer array nums, return an array answer such that answer[i]
        is equal to the product of all the elements of nums except nums[i].

        The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

        You must write an algorithm that runs in O(n) time and
        without using the division operation.
        """
        #create result array size of nums with 1
        res = [1] * len(nums)
        #set prefix to 1
        prefix = 1
        #go through array forward and multiply by all previous values and set val in res[i]
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        #go through nums in reverse order and multiply res by postfix
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        #should have array of all values
        return res