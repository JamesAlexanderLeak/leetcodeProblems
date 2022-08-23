# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, return its maximum depth.

       A binary tree's maximum depth is the number of nodes along the 
       longest path from the root node down to the farthest leaf node.
        """
        #create "global" maxDepth 
        self.maxDepth = 0
        def findDepth(node):
            #recurse through left and right sides and return depth to left and right
            if not node:
                return 0
            left,right = findDepth(node.left),findDepth(node.right)
            #set max Depth to 1 + max of left and right
            maxD = 1+ max(left,right)
            #set globalMaxDepth to current and new
            self.maxDepth = max(self.maxDepth,maxD)
            #return 1 + max of left and right
            return 1 + max(left,right)
            
        findDepth(root)
        return self.maxDepth