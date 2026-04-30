class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        islands = [(row, col) for row in range(len(grid)) for col in range(len(grid[0])) if grid[row][col] == "1"]
        visited = set()
        count = 0
        while islands:
            curr_coor = islands.pop()
            while islands and curr_coor in visited:
                curr_coor = islands.pop()
            if curr_coor in visited:
                continue
            queue = deque([curr_coor])
            count += 1
            while queue:
                row, col = queue.popleft()
                visited.add((row, col))
                for d_row, d_col in directions:
                    new_row = row + d_row
                    new_col = col + d_col
                    if min(new_row, new_col) < 0 or new_row >= len(grid) or new_col >= len(grid[0]) or (new_row, new_col) in visited or grid[new_row][new_col] == "0":
                        continue
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))
        return count