# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if sum == root.val and not root.left and not root.right:
            return True
        sumRemain = sum - root.val
        return self.hasPathSum(root.left, sumRemain) or self.hasPathSum(root.right, sumRemain)