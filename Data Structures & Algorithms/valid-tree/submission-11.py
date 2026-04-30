class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        stack = [(None, 0)]
        visited = set()
        
        while stack:
            # i want to add to the stack all the descedants
            parent_node, curr_node = stack.pop()
            if curr_node in visited:
                return False
            visited.add(curr_node)
            # last in first out
            for nei in adj[curr_node]:
                if nei == parent_node:
                    continue
                stack.append((curr_node, nei))
        return len(visited) == n