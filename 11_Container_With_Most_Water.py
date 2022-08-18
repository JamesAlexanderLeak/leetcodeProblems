from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        You are given an array height of length n.
        There are n vertical lines drawn such that the two
        endpoints of the ith line are (i,0) and (i,height[i]).

        Find two lines that together with the x-axis form a container,
        such that the container contains the most water.

        Return the maximum water a container can store.
        """
        #two pointers, left and right
        left,right = 0,len(height)-1
        #set initial volume to 0
        vol = 0
        #while pointers don't cross
        while left <= right:
            #volume is max of cur vol and new volume of pointer
            vol = max(vol,min(height[left],height[right])*(right-left))
            #if height of left is less than height of right, move left pointer forward
            if height[left] < height[right]:
                left+= 1
            #else, move right pointer back
            else:
                right-= 1
        #return volume
        return vol
            