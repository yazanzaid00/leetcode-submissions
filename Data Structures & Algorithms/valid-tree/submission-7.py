class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)#can I make the adjancy list instead of list a set? does this help anything i'll try agian later...
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited = [False] * n
        parent = [None] * n
        # tree is defined acyclic + connected, we can do DFS and check for cycle + connected
        # check if acyclic, two approach slow + fast pointer, or regular dfs while checking if visited and is true and visited again means there is a cycle
        def dfs_acycle(i: int):
            if visited[i]:
                return False
            visited[i] = True
            neighbours = adj_list[i]
            for nei in neighbours:
                if parent[i] == nei:
                    continue
                parent[nei] = i
                # propogate cycle check
                if dfs_acycle(nei) == False:
                    return False
            return True

        return dfs_acycle(0) and all(visited[node] for node in range(1, n))
            



