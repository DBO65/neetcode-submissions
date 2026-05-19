# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(r1, r2):
            if r1 == r2 == None:
                return True     
            if r1 and r2 and r2.val == r1.val:
                return dfs(r1.left, r2.left) and dfs(r1.right, r2.right)
            return False
              
        return dfs(p, q)