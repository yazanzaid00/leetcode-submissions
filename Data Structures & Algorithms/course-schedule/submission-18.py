class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         I meant empty such as empty cells real empty cells how to have empty 2d board in python
# I mean something like this:
# adj_list = [[] * numCourses for _ in range(numCourses)] to have numCourses empty cells allocated for each row... 
        adj_list = [[] for _ in range(numCourses)]
        for post, pre in prerequisites:
            if pre == post:
                return False
            adj_list[pre].append(post)
        # detect cycle using bfs?
        queue = deque([0])
        visited = [False] * numCourses
        while queue:
            curr_node = queue.popleft()
            # visited its children
            for node in adj_list[curr_node]:
                print(visited)
                print(node)
                if visited[node]:
                    return False
                visited[node] = True
                queue.append(node)

        return True
