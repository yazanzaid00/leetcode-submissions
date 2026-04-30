"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Map each node to its copy, then recreate?
        if not node:
            return None
        copy = dict()
        # bfs
        queue = deque([node])
        visited = set([node])
        while queue:
            cur_node = queue.popleft()
            copy[cur_node] = Node(cur_node.val)
            for nei in cur_node.neighbors:
                if nei in visited:
                    continue
                queue.append(nei)
                visited.add(nei)
        
        # now we have copies, create the map
        queue = deque([node])
        visited = set([node])
        while queue:
            cur_node = queue.popleft()
            for nei in cur_node.neighbors:
                copy[cur_node].neighbors.append(copy[nei])
                if nei in visited:
                    continue
                queue.append(nei)
                visited.add(nei)

        return copy.get(node)