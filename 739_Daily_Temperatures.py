from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Given an array of integers temperatures represents the daily
        temperatures, return an array answer such that answer[i] is the
        number of days you have to wait after the ith day to get a warmer
        temperature. If there is no future day for which this is possible,
        keep answer[i] == 0 instead.
        """
        #create result array of size temperatures
        res = [0] * len(temperatures)
        #create stack with pair of [temp: index]
        stack = []#pair: [temp: index]
        #for i (index), t (temperature)
        for i,t in enumerate(temperatures):
            #while stack is not empty
            #and temp is greater than top of stack
            #This will pop all temperatures less than current temp.
            while stack and t > stack[-1][0]:
                #stackTemp,stackIndex
                stackT,stackInd = stack.pop()
                #result[index] = (currentIndex - stackIndex)
                res[stackInd] = (i-stackInd)
            #append current temperature and index to stack
            stack.append([t,i])
        #return result
        return res