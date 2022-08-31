from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums of unique elements, 
        return all possible subsets (the power set).

        The solution set must not contain duplicate subsets. 
        Return the solution in any order.
        """

        #backtracking problem
        #create result array
        res = []
        #create subset array
        subset = []
        #define dfs search
        def dfs(i):
            print("subset",subset)
            #if all elements of list have been iterated through (i >= len(nums))
            if i >= len(nums):
                #adds current subset to res
                res.append(subset.copy())
                print("res",res)
                return
            #include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            #decision to not include nums[i]
            subset.pop()
            #call again
            dfs(i+1)
        dfs(0)
        return res

newSol = Solution()
print(newSol.subsets(nums=[1,2,3]))
