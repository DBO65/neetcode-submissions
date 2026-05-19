# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(r1, r2):
            if r1 == r2 == None:
                return True
            if r1 and r2 and (r1.val == r2.val):
                return sameTree(r1.left, r2.left) and sameTree(r1.right, r2.right)
            return False
        
        if root == subRoot == None:
            return True        
        if root and not subRoot:
            return True
        if not root and subRoot:
            return False
        if sameTree(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    


        