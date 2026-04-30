class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # check if directed graph is acyclic (it can be multiple trees, this is ok no need for connectivity such as [1,2] [3,4])
        adj_list = defaultdict(list)
        for post, pre in prerequisites:
            adj_list[pre].append(post)
        # 0 -> unvisited, 1->visiting, 2-> visited
        visited = [0] * numCourses
        parent = [None] * numCourses
        # check if there is a cycle using DFS
        def cycle_dfs(i: int):
            # we can do the checks in here
            if visited[i] == 1:
                return True
            visited[i] = 1 # pre visit
            neighbours = adj_list[i] # check neighbours
            for nei in neighbours:
                # or in here # nei = 0 parent[i] = None
                # if nei == parent[i]:
                #     continue
                parent[nei] = i
                if cycle_dfs(nei):
                    return True # propgate the result to the caller...
            visited[i] = 2 # post visit                
            return False

        for i in range(numCourses):
            if visited[i] == 0:
                if cycle_dfs(i):
                    return False
        
        return True