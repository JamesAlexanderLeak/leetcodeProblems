class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Given an interger array nums, return true if any value
        appears at least twice in the array, and
        return false if every element is distinct
        """
        #create set of nums input
        numsSet = set(nums)
        #if the len of the set is equal to the len of the input, return false
        if len(numsSet) == len(nums):
            return False
        #else return True
        return True