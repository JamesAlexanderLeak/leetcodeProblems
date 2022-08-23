# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Given a binary tree, determine if it is height-balanced.

        For this problem, a height-balanced binary tree is defined as:
            a binary tree in which the left and right subtrees of every node 
            differ in height by no more than 1.
        """
        #def check func
        def check(root):
            #if leaf node, return 0
            if root is None:
                return 0
            #get left and right trees heights
            left = check(root.left)
            right = check(root.right)
            #if -1 (failure of heights has occurred in previous subtree, return -1)
            #or if heights differ by more than 1 absolute value of (left-right) > 1
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            #else, return max height of left and right subtrees
            return 1 + max(left,right)
        #check if check has failed and return result.
        return check(root) != -1