# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root

        L = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1 : L + 1], inorder[:L])
        root.right = self.buildTree(preorder[L + 1 :], inorder[L + 1 :])
        return root