from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Given the roots of two binary trees root and subRoot, return true
        if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

        A subtree of a binary tree tree is a tree that consists of a node in tree 
        and all of this node's descendants. The tree tree could also be considered as a subtree of itself.
        """
        
        def checkTrees(root1,root2):
            #pulled code from previous "check Tree" problem. Problem 100.
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
        
        def findStart(startRoot,subRoot):
            if startRoot is None:
                return False
            if startRoot.val == subRoot.val:
                if checkTrees(startRoot,subRoot):
                    return True
            if findStart(startRoot.left,subRoot) or findStart(startRoot.right,subRoot):
                return True
            return False
        if findStart(root,subRoot):
            return True
        return False
            