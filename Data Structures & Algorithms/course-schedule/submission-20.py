class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        in_deg = [0] * numCourses
        for course, pre in prerequisites:
            adj[pre].append(course)
            in_deg[course] += 1
        queue = deque([course for course in range(numCourses) if in_deg[course] == 0])
        taken = 0
        while queue:
            curr_course = queue.popleft()
            taken += 1
            for nxt_course in adj[curr_course]:
                in_deg[nxt_course] -= 1
                if in_deg[nxt_course] == 0:
                    queue.append(nxt_course)
        return taken == numCourses