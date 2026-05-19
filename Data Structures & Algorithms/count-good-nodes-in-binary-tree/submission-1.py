# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxi):
            l = r = 0
            count = 1
            if not root:
                return 0
            count = 1 if root.val >= maxi else 0
            maxi = max(maxi, root.val)
            count += dfs(root.left, maxi)
            count += dfs(root.right, maxi)  
            return count
        
        return dfs(root, root.val)
            
        

        
        