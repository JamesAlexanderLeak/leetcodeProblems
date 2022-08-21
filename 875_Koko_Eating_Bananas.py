from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Koko loves to eat bananas. 
        There are n piles of bananas, the ith pile has piles[i] bananas.
        The guards have gone and will come back in h hours.

        Koko can decide her bananas-per-hour eating speed of k.
        Each hour, she chooses some pile of bananas and eats k bananas from that pile.
        If the pile has less than k bananas, she eats all of them instead and 
        will not eat any more bananas during this hour.

        Koko likes to eat slowly but still wants to finish eating all the 
        bananas before the guards return.

        Return the minimum integer k such that she can eat all the 
        bananas within h hours.
        """
        #binary search for min rate k
        #left is 1 since that is smallest rate and max rate is max number in piles
        l,r = 1,max(piles)
        #
        k = 0
        while l <= r:
            #binary search
            hours = 0
            mid = (l+r) //2
            #iterating through piles to calculate hours
            for p in piles:
                hours+= math.ceil(p/mid)
            if hours > h:
                #if hours is greater than input, move left pointer 
                l = mid+1
            else:
                #otherwise, set k and move right
                k = mid
                r = mid-1
        return k