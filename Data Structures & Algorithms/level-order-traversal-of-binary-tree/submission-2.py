# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        sol = []
        q = deque([root])
        level = 1

        while q:
            levelList = []
            length = len(q)

            for i in range(length):
                node = q.popleft()
                if node and node != "None":
                    q.append(node.left) if node.left else q.append("None")
                    q.append(node.right) if node.right else q.append("None")
                if node == "None":
                    continue
                levelList.append(node.val)
            sol.append(levelList) if levelList else None
        return sol
        