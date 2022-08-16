class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsSet = set(nums)
        if len(numsSet) == len(nums):
            return False
        return True