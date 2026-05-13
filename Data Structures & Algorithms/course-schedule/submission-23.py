class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Detect whether the directed prerequisite graph has a cycle.
        adj_list = {}
        for nxt, pre in prerequisites:
            if pre not in adj_list:
                adj_list[pre] = list()
            adj_list[pre].append(nxt)

        state = [0] * numCourses  # 0 = unvisited, 1 = visiting, 2 = done

        def detect_cycle(node):
            if state[node] == 2:
                return False
            if state[node] == 1:
                return True

            state[node] = 1
            if node in adj_list:
                for nei in adj_list[node]:
                    if detect_cycle(nei):
                        return True

            state[node] = 2
            return False

        for course in range(numCourses):
            if detect_cycle(course):
                return False

        return True