from typing import List

class Solution:
    def topKFrequent(self,nums: List[int],k: int) -> List[int]:
        """
        Given an integer array nums and an integer k, return the k most frequent elements.
        You may return the answer in any order.
        """
        #create a dictionary called count
        count = dict()
        #create an array of arrays called freq
        freq = [[] for i in range(len(nums)+1)]
        #for number in nums, set count[number] = frequency of number
        for n in nums:
            count[n] = 1 + count.get(n,0)
        #for key(number), value(count) in dictionary, append number to freq[count]
        for n,c in count.items():
            freq[c].append(n)
        #create result
        res = []
        #iterate backwards in freq and append values to result until k==len(result)
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
