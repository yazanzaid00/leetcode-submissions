class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list =[[] for _ in range(n)]
        parent = [None] * n
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # dfs if visisted again means there is acycle -> not tree
        visited = [False] * n
        def dfs(start_node):
            if visited[start_node]:
                return False
            visited[start_node] = True
            neighbours = adj_list[start_node]
            for nei in neighbours:
                if parent[start_node] == nei:
                    continue
                parent[nei] = start_node
                if dfs(nei) == False:
                    return False
            return True
        if dfs(0) == False:
            return False
        return all (visited[i] for i in range(n))
