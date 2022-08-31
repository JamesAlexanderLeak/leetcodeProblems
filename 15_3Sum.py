from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
        such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

        Notice that the solution set must not contain duplicate triplets.
        """
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        for i,a in enumerate(nums):
            #skip repeated values
            if i > 0 and a == nums[i-1]:
                continue
            #two pointers
            l,r = i+1,len(nums)-1
            #while not crossing
            while l<r:
                #compute threeSum
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r-= 1
                elif threeSum < 0:
                    l+= 1
                else:
                    #if threeSum == 0, append to result
                    res.append([a,nums[l],nums[r]])
                    #move left forward by one
                    l+=1
                    #while not repeated value and not crossing
                    while nums[l] == nums[l-1] and l< r:
                        l+= 1
        return res