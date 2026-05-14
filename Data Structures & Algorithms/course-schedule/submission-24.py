class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        for course, prev in prerequisites:
            adj_list[prev].append(course)
        
        state = [0] * numCourses # 0 unvisisted, 1 visitng, 2 visisted
        def detect_cycle(node: int) -> bool:
            if state[node] == 1:
                # visitng already there is a cycle
                return True
            if state[node] == 2:
                return False
            
            state[node] = 1

            for nei in adj_list[node]:
                if detect_cycle(nei):
                    return True

            state[node] = 2
            return False

        
        for course in range(numCourses):
            if detect_cycle(course):
                return False
        
        return True
        