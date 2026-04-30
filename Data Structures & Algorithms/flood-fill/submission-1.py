class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # dfs solves this nicely
        directions = [ 
        (0, 1), # right
        # (1, 1), #bottom right
        (1, 0), # bottom
        # (1, -1), # bottom left
        (0, -1), # left
        # (-1, -1), # upper left
        (-1, 0), # upper
        # (-1, 1) # upper right
        ]
        visited = [[False]*len(image[0]) for _ in range(len(image))]
        def dfs(sr: int, sc: int):
            if visited[sr][sc]:
                return
            visited[sr][sc] = True
            # nonlocal color # should i type this?
            orig = image[sr][sc]
            image[sr][sc] = color
            for hor, vert in directions:
                # sr, sc += hor, vert can I do this in one liner? i mean for future reference so i can learn
                new_sr = sr + hor
                new_sc = sc + vert
                # is the orig color transistive? i believe so
                if min(new_sr, new_sc) < 0 or new_sr >= len(image) or new_sc >= len(image[0]) or image[new_sr][new_sc] != orig:
                    continue
                # visit new valid ones
                dfs(new_sr, new_sc)

        dfs(sr, sc)
        return image