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
            return None
        # we need to move over
        # original -> cloned
        cloned_dict = {}
        visited = set()
        def dfs(node):
            if not node or node in visited:
                return
            visited.add(node)
            if node not in cloned_dict:
                cloned_dict[node] = Node(node.val)
            for nei in node.neighbors:
                if nei not in cloned_dict:
                    cloned_dict[nei] = Node(nei.val)
                cloned_dict[node].neighbors.append(cloned_dict[nei])
                dfs(nei)

        dfs(node)

        return cloned_dict[node]
