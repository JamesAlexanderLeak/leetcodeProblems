from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Given n pairs of parentheses, write a function to
        generate all combinations of well-formed parenthesis

        Example: n = 3
        Output = ["((()))","(()())","(())()","()(())","()()()"]
        """
        #backtracking problem since it is asking for ~combinations~
        #create result array
        res = []
        #curParens is stack that holds parentheses.
        curParens = []
        #define backTrack function to recurse through
        def backTrack(left,right,current):
            #if leftCount, rightCount are equal
            #same number of parentheses opened and closed
            #and are equal to input n, append to result
            if left == right == n:
                res.append("".join(current))
            #if left < n (need to open more parentheses '(')
            #append to current and recurse with count to left + 1
            if left < n:
                current.append('(')
                backTrack(left+1,right,current)
                #after backtracked, pop value
                current.pop()
            #if right < left (need to close parenthese ')')
            #append to current and recurse with count to right +1
            if right < left:
                current.append(')')
                backTrack(left,right+1,current)
                #after backtracked, pop right
                current.pop()
        #start function with 0 on left and 0 on right and empty curParens
        backTrack(0,0,curParens)
        return res