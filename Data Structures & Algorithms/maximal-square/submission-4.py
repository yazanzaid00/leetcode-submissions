class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp[i][j] = maximum square side length that bottom right is i, j
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        max_area = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    max_area = max(
                        dp[i][j] ** 2,
                        max_area
                    )

        return max_area