from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        l, r = 0, n - 1

        # process outer ring, then move inward
        while l < r:
            top, bottom = l, r

            # Q: how many 4-cell rotations do we need for this ring?
            for i in range(r - l):
                # Top-left cell for this cycle is at (top, l + i)
                # Bottom-left is at (bottom - i, l)
                # Bottom-right is at (bottom, r - i)
                # Top-right is at (top + i, r)

                # 1) Save top-left before overwriting it
                # TODO: store matrix[top][l + i] in a temp variable (e.g., top_left)
                top_left = matrix[top][l + i]

                # 2) Move bottom-left -> top-left
                # TODO: matrix[top][l + i] = matrix[...][...]
                matrix[top][l + i] = matrix[bottom-i][l]

                # 3) Move bottom-right -> bottom-left
                # TODO: matrix[bottom - i][l] = matrix[...][...]
                # matrix[bottom - i][l] = ...
                matrix[bottom-i][l] = matrix[bottom][r - i]
                # 4) Move top-right -> bottom-right
                # TODO: matrix[bottom][r - i] = matrix[...][...]
                # matrix[bottom][r - i] = ...
                matrix[bottom][r - i] = matrix[top + i][r]
                # 5) Move saved top-left -> top-right
                # TODO: matrix[top + i][r] = temp
                # matrix[top + i][r] = ...
                matrix[top + i][r] = top_left
            # move to the next inner ring
            l += 1
            r -= 1