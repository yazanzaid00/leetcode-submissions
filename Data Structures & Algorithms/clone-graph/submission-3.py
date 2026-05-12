"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        clone_dict = defaultdict(Node)
        clone_dict[node.val] = Node(node.val)
        # bfs
        queue = deque([node])
        visited = set([node.val])
        while queue:
            cur_node = queue.popleft()
            for nei in cur_node.neighbors:
                if nei.val not in visited:
                    visited.add(nei.val)
                    # the key can be the Node it self? or it can be the vale if i know the value is unique
                    clone_dict[nei.val] = Node(nei.val)
                    queue.append(nei)
                clone_dict[cur_node.val].neighbors.append(clone_dict[nei.val])
        return clone_dict[node.val]