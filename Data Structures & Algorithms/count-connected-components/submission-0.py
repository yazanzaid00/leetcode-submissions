class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited = [False] * n
        
        def dfs(source_node):
            visited[source_node] = True
            neighbours = adj_list[source_node]
            for node in neighbours:
                if visited[node]:
                    continue
                visited[node] = True
                dfs(node)
            


        counter = 0
        # for each node visit its neighbours
        for i in range(n):
            if visited[i] == False:
                dfs(i)
                counter += 1
        return counter