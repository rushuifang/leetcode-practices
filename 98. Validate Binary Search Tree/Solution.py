# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper (node, lower = float("-inf"), higher = float("inf")):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= higher:
                return False
            
            return helper(node.left, lower, val) and helper(node.right, val, higher)
        
        return helper(root)