# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, mini, maxi):
            if not node:
                return True
            if not (mini < node.val < maxi):
                return False

            return valid(node.left, mini, node.val) and valid(node.right, node.val, maxi)

        return valid(root, -1001, 1001)