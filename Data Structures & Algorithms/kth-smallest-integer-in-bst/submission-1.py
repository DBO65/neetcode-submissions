# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:      
        self.sol = None

        def dfs(root, cnt):            
            if not root:
                return cnt 

            cnt = dfs(root.left, cnt)
            
            if cnt == 1:
                self.sol = root.val
            if cnt >= 1:
                cnt -=  1  
            
            cnt = dfs(root.right, cnt)

            return cnt

        dfs(root, k)
        return self.sol