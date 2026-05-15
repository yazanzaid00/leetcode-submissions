class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        in_deg = [0] * numCourses
        for course, prev in  prerequisites:
            adj_list[prev].append(course)
            in_deg[course] += 1

        queue = deque([course for course in range(numCourses) if in_deg[course] == 0])
        taken = 0
        while queue:
            cur_course = queue.popleft()
            taken += 1
            for nei in adj_list[cur_course]:
                in_deg[nei] -= 1
                if in_deg[nei] == 0:
                    queue.append(nei)
        
        return taken == numCourses
