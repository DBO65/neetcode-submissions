# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """equivilent = True
        def dfs(pNode, qNode):
            nonlocal equivilent 

            if not pNode and not qNode:
                return 
            if not pNode and qNode:
                equivilent = False
            if not qNode and pNode:
                equivilent = False
            if pNode != qNode:
                equivilent = False
            
            dfs(pNode.left, qNode.left)
            dfs(pNode.right, qNode.right)   

            return equivilent          

        if not p or not q:
            return False
        if not p and q:
            return False
        if not p and not q:
            return True 

        dfs(p, q)
        return equivilent"""
        
        if not p and not q:
            return True 
        if not p or not q or p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


        