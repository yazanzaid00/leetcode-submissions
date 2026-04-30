class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        def dfs(i, j):
            if  i <= -1 or j <= -1 or i == len(grid) or j == len(grid[0]) or visited[i][j] or grid[i][j] == '0':
                return
            # grid grid[i][j] == '1'
            visited[i][j] = True
            # visit its neighbours
            dfs(i, j+ 1) # visit right neighbour
            dfs(i + 1, j) # visit left neighbour
            dfs(i - 1, j)
            dfs(i, j - 1)

        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == '1':
                    dfs(i,j)
                    counter += 1
        return counter