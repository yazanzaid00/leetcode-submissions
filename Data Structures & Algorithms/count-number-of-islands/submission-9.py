class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        if len(grid) <= 1 and len(grid[0]) <= 1:
            return int(grid[0][0])
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        def dfs(row=0, col=0):
            # I need to count once for each coordinate,
            count = 0
            if grid[row][col] == "1":
                visited.add((row, col))
                for dir in directions:
                    # surroundings
                    new_row, new_col = row + dir[0], col + dir[1]
                    if min(new_row, new_col) < 0 or \
                       new_row >= rows or new_col >= cols or (new_row, new_col) in visited:
                       continue
                    count = 1      
                    dfs(new_row, new_col)
                    
            return count

        counter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    counter += dfs(row, col)
        return counter