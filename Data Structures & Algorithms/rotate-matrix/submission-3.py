from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        left, right = 0, n - 1  # current layer boundaries

        # Process layers from outside in
        while left < right:
            top, bottom = left, right  # because square matrix

            # How many 4-cycles in this ring?  side_length - 1
            for offset in range(right - left):
                # Each offset corresponds to a "square" of 4 positions in this ring

                # TODO: derive the 4 coordinates from the drawing:
                # top-left position
                r1, c1 = top, left + offset       # this one is given

                # bottom-left position
                r2, c2 = bottom - offset, left                 # TODO

                # bottom-right position
                r3, c3 = bottom, right - offset               # TODO

                # top-right position
                r4, c4 = top + offset, right                 # TODO

                # Now rotate the 4 values clockwise using ONE temp
                temp = matrix[r1][c1]             # save top-left

                # bottom-left -> top-left
                matrix[r1][c1] = matrix[r2][c2]              # TODO: which (r,c)?

                # bottom-right -> bottom-left
                matrix[r2][c2] = matrix[r3][c3]              # TODO

                # top-right -> bottom-right
                matrix[r3][c3] = matrix[r4][c4]              # TODO

                # saved top-left -> top-right
                matrix[r4][c4] = temp             # TODO

            # Move inward to the next ring
            left += 1
            right -= 1
