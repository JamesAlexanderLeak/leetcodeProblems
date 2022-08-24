from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode],low=float('-inf'),hi=float('inf')) -> bool:
        #if leaf, return True
        if not root:
            return True
        #if cur val is not between low and high, return False
        if not low < root.val < hi:
            return False
        #traverse down left and right and check if values are in valid range.
        #return if both left and right subtrees are True.
        #have to get min,max of self and high/low to ensure left/right subtrees are within
        #bounds of the current value or overall subtree max/min value
        return self.isValidBST(root.left,low,min(root.val,hi)) and self.isValidBST(root.right,max(low,root.val),hi)
    