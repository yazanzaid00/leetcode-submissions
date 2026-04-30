class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions =[
            (-1, 0),
            (1, 0),
            (0, 1),
            (0, -1)
        ]
        def dfs(i: int, j:int) -> None:
            if min(i,j) < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for d_i, d_j in directions:
                new_i, new_j = i + d_i, j + d_j
                dfs(new_i, new_j)
            return
        
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count