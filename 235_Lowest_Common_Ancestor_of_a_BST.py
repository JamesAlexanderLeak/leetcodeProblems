# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Given a binary search tree (BST), 
        find the lowest common ancestor (LCA)
        node of two given nodes in the BST.

        According to the definition of LCA on Wikipedia: 
        “The lowest common ancestor is defined between two nodes p and q as the lowest node in T
        that has both p and q as descendants (where we allow a node to be a descendant of itself).”
        """
        #low is min of val p,q, high is max
        low = min(p.val,q.val)
        high = max(p.val,q.val)
        #if cur is between low and high, return
        if (high >= root.val and low <= root.val):
            return root
        #if either value is equal to cur, return cur
        elif high == root.val or low == root.val:
            return root
        #search left if low and high are lower
        elif low <= root.val and high <= root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        #search right if low and high are higher
        elif high >= root.val and low >= root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        