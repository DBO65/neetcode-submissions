"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return 
        oldNew = {}

        def dfs(node):
            if node in oldNew:
                return oldNew[node]

            cpy = Node(node.val)
            oldNew[node] = cpy
            
            for nbr in node.neighbors:
                cpy.neighbors.append(dfs(nbr))

            return cpy
        
        return dfs(node)


        """if not node:
            return 
        
        seen = set()
        root = node

        def dfs(node):
            nonlocal seen, root 

            stack = [node]
            while stack:
                node_og = stack.pop()
                root = Node(node_og.val)

                if node_og.neighbors:
                    for nbr in node_og.neighbors:
                        stack.append(nbr)
                        root.neighbors.append(nbr)
                        seen.add(nbr)
            return root

        return dfs(node)"""

        