from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Given an array of integers nums which is sorted in ascending order,
        and an integer target, write a function to search target in nums.
        If target exists, then return its index. Otherwise, return -1.

        You must write an algorithm with O(log n) runtime complexity.
        """

        #typical binary search algorithm on sorted array
        #left and right pointers at beginning and end of arr
        left,right = 0,len(nums)-1
        #while left <= right
        while(left <= right):
            #mid = left + (right index - left index)//2 for integer division
            mid = left + (right - left)//2
            #if equal, return index
            if nums[mid] == target:
                return mid
            #if mid is greater than target, reduce right
            elif nums[mid] > target:
                right = mid-1
            #if mid is less than target, increase left
            elif nums[mid] < target:
                left = mid+1
        #else, return -1
        return -1
    