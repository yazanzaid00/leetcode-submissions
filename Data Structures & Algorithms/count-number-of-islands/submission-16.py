class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions =[
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1)
        ]
        def dfs(i: int, j:int) -> None:
            if min(i,j) < 0 or i >= len(grid) or j >= len(grid[0]) or visited[i][j] or grid[i][j] == "0":
                return
            visited[i][j] = True
            for d_i, d_j in directions:
                new_i, new_j = i + d_i, j + d_j
                dfs(new_i, new_j)
            return
        

        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count