from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Given the root of a binary search tree, and an integer k,
        return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
        """
        stack = []
        curr = root
        #while stack is still nonempty or curr is not leaf
        while stack or curr:
            #while not leaf, iterate left to find smaller values (moving through left side of tree)
            while curr:
                #append to stack
                stack.append(curr)
                curr = curr.left
            #once hit leaf, pop stack to go back to value
            curr = stack.pop()
            #subtract k by 1
            k-= 1
            #if k == 0 (at kth smallest value), return k
            if k == 0:
                return curr.val
            #otherwise, continue iterating through tree
            curr = curr.right
            