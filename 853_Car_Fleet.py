from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        There are n cars going to the same destination along a one-lane road.
        The destination is target miles away.
        
        You are given two integer array position and speed, both of length n,
        where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).
        
        A car can never pass another car ahead of it, but it can catch up to it
        and drive bumper to bumper at the same speed.
        The faster car will slow down to match the slower car's speed.
        The distance between these two cars is ignored (i.e., they are assumed to have the same position).
        
        A car fleet is some non-empty set of cars driving at the same position and same speed. 
        Note that a single car is also a car fleet.
        
        If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.
        
        Return the number of car fleets that will arrive at the destination.
        """
        
        if len(position) <=1:
            return 1
        #zip up pairs and speed for ease
        pairs = [[p,s] for p,s in zip(position,speed)]
        #create stack
        stack = []
        #sort based on position and iterate through list in reverse
        #trying to find rate of cars to find if groups are created, so go in reverse
        #O(n log n) for sorted (time complexity is O(n log n))
        for p,s in sorted(pairs)[::-1]:
            #append time when car reaches end end of list
            stack.append((target-p) /s)
            """
            iterating through list in reverse order so building stack backwards
            if top of stack (previous car if iterating through forwards) reaches
            destination before second to top stack (next car if iterating through forwards),
            need to group the cars and keep the slower one (the second to top stack), so pop()
            and continue iterating backwards.
            Continually perform this step to group more cars.
            """
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        #length of stack is number of car fleets since popping removes a car (grouping the cars)
        return len(stack)
    