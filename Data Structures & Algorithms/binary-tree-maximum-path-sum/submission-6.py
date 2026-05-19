# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxPath = -10000

        def dfs(root):
            if not root:
                return 0
            l = dfs(root.left)
            r = dfs(root.right)

            newPath = l + r + root.val
            if newPath > self.maxPath:
                self.maxPath = newPath
            
            retPath = root.val + max(l, r, 0)
            if retPath > self.maxPath:
                self.maxPath = retPath
            
            return retPath


        if root.right == root.left == None: return root.val
        dfs(root)
        return self.maxPath
            