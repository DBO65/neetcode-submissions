# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True 
        def dfs(node):
            if not node:
                return 0

            left = right = 0

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                self.balanced = False
            
            return max(left, right) + 1

        
        if not root:
            return True

        dfs(root)
        return self.balanced


        
        