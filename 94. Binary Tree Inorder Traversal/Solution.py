# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []

        def helper(root):
            if root:
                if root.left:
                    helper(root.left)
                res.append(root.val)
                if root.right:
                    helper(root.right)

        helper(root)
        return res