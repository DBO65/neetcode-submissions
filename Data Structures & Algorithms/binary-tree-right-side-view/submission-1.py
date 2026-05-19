# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        sol = []
        q = collections.deque([root])

        while q:
            length = len(q)
            rSide = None

            for i in range(length):
                node = q.popleft()
                if node:
                    rSide = node
                    q.append(node.left)  
                    q.append(node.right)
            if rSide:
                sol.append(rSide.val)
        return sol


