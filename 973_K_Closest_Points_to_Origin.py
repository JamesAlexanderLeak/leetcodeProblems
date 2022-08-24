from typing import List 
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        Given an array of points where points[i] = [xi, yi] 
        represents a point on the X-Y plane and an integer k, 
        return the k closest points to the origin (0, 0).

        The distance between two points on the X-Y plane is 
        the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

        You may return the answer in any order. 
        The answer is guaranteed to be unique (except for the order that it is in).
        """
        ans = []
        distances = []
        #calculate distances with distance equation (don't need sqrt)
        for x,y in points:
            #abs(x2-x1)^2 + abs(y2-y1)^2

            dist = (abs(x-0) ** 2) + (abs(y-0) ** 2)
            distances.append([dist,x,y])
        #creates minheap
        heapq.heapify(distances)
        #heap pop k number of times and append values to ans.
        for _ in range(K):
            dist,x,y = heapq.heappop(distances)
            ans.append([x,y])
        #return ans
        return ans