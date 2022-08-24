from typing import List
import heapq
from collections import deque,Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Given a characters array tasks, representing the tasks a CPU needs to do, 
        where each letter represents a different task. Tasks could be done in any order. 
        Each task is done in one unit of time. For each unit of time, 
        the CPU could complete either one task or just be idle.

        However, there is a non-negative integer n that represents the cooldown period
        between two same tasks (the same letter in the array),
        that is that there must be at least n units of time between any two same tasks.

        Return the least number of units of times that the CPU 
        will take to finish all the given tasks.
        """
        #counter will create a dictionary of values
        count = Counter(tasks)
        #set values to negative for max heap
        maxHeap = [-cnt for cnt in count.values()]
        #heapify maxHeap
        heapq.heapify(maxHeap)
        #start timer
        time = 0
        #queue
        q = deque()
        #while values in maxHeap or queue
        while maxHeap or q:
            #increase timer by 1
            time += 1
            #if maxHeap is empty, set time to next value in queue (fast forward)
            if not maxHeap:
                time = q[0][1]
            #"decrease" number of tasks
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                #if cnt is not 0, append value to queue
                if cnt:
                    #(count,futureTime when task is ready)
                    q.append([cnt,time+n])
            #if value in queue and futureTime == curTime, push back onto maxHeap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap,q.popleft()[0])
        #return time taken
        return time