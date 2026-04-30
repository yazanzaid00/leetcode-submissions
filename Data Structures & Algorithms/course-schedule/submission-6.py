class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for course, pre in prerequisites:
            adj_list[pre].append(course)
        visit = [ 0 ] * numCourses
        def dfs(node):
            neighbours = adj_list[node]
            visit[node] = 1
            for nei in neighbours:
                # if visiting problematic
                if visit[nei] == 1:
                    return False
                if visit[nei] == 2:
                    continue
                if dfs(nei) == False:
                    return False
            # visited completely, I can also make it inise the for loop, which one is better pratcice?
            visit[node] = 2
            return True

        for i in range(numCourses):
            # already visited
            if visit[i] == 2:
                continue
            if (dfs(i) == False):
                return False
        return True