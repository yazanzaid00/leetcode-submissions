class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "0":
                    continue
                islands += 1
                queue = deque([(row, col)])
                while queue:
                    row, col = queue.popleft()
                    grid[row][col] = "0"
                    for d_row, d_col in directions:
                        new_row, new_col = row + d_row, col + d_col
                        if min(new_row, new_col) < 0 or new_row >= len(grid) or new_col >= len(grid[0]) or grid[new_row][new_col] == "0":
                            continue
                        
                        queue.append((new_row, new_col))
        return islands