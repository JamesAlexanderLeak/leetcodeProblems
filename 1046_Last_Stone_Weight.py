from typing import List
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        You are given an array of integers stones where stones[i] is the weight of the ith stone.

        We are playing a game with the stones.
        On each turn, we choose the heaviest two stones and smash them together.
        Suppose the heaviest two stones have weights x and y with x <= y.
        
        The result of this smash is:
            If x == y, both stones are destroyed, and
            If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
        
        At the end of the game, there is at most one stone left.

        Return the weight of the last remaining stone.
        If there are no stones left, return 0.
        """
        #create max heap with negative number (heapq is a min heap)
        stones = [-s for s in stones]
        #heapify stones
        heapq.heapify(stones)
        #while there are 2 values in stones
        while len(stones) > 1:
            #heappop top 2 elements
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            #if they are not equal, push result onto heapq
            if y > x:
                heapq.heappush(stones,x-y)
        #append 0 to end, if array is empty, will be result
        stones.append(0)
        #return first val of stones
        return abs(stones[0])
            
        