from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Given the roots of two binary trees p and q, write a function to check if they are the same or not.

        Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
        """
        #iterate through both trees and check vals, left subtrees and right subtrees.
        def checkTrees(root1,root2):
            #if leaves are none, return True
            if root1 is None and root2 is None:
                return True
            #if one has a node and other has a leaf, return False
            if (root1 is None and root2 is not None) or (root1 is not None and root2 is None):
                return False
            #if values are not the same, return False
            if root1.val != root2.val:
                return False
            #if left subtrees are not equal, return False
            if not checkTrees(root1.left,root2.left):
                return False
            #if right subtrees are not equal, return False
            if not checkTrees(root1.right,root2.right):
                return False
            #otherwise return True
            return True
        
        return checkTrees(p,q)