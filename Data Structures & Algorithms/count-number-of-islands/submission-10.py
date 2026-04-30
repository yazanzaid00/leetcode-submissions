class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(coordinate):
            row, col = coordinate
            if min(row, col) < 0 or row >= rows or col >= cols or grid[row][col] == "0" or (row, col) in visited:
                return
            visited.add((row, col))
            for dir in directions:
                new_row, new_col = row + dir[0], col + dir[1]
                dfs((new_row, new_col))

        counter = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs((row, col))
                    counter += 1

        return counter
