class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                islands += 1
                # mark as visited
                grid[i][j] = "0"
                queue = deque([(i, j)])
                while queue:
                    row, col = queue.popleft()
                    for d_row, d_col in directions:
                        new_row, new_col = row + d_row, col + d_col
                        if min(new_row, new_col) < 0 or new_row >= len(grid) or new_col >= len(grid[0]) or grid[new_row][new_col] == "0":
                            continue
                        # mark as visited
                        grid[new_row][new_col] = "0"
                        # want to visits its children later on
                        queue.append((new_row, new_col))
        return islands