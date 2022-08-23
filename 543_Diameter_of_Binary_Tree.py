from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Given the root of a binary tree, return the length of the diameter of the tree.

        The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

        The length of a path between two nodes is represented by the number of edges between them.
        """
        #extremely similar to 104. Maximum Depth of Binary Tree
        self.ans = 0
        def maxD(node):
            if not node:
                return 0
            left,right = maxD(node.left),maxD(node.right)
            self.ans = max(self.ans,left+right)
            return 1 + max(left,right)
        maxD(root)
        return self.ans