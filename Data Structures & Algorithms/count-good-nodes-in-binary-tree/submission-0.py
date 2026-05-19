# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxi = -101
        count = 0

        def dfs(root, maxi, count):
            l = r = count = 0
            if not root:
                return count
            if root.val >= maxi:
                maxi = root.val
                count += 1
            l += dfs(root.left, maxi, count)
            r += dfs(root.right, maxi, count)  
            count +=  l + r     
            return count
        
        return dfs(root, -101, 0)
            
        

        
        