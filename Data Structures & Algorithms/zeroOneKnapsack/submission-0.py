class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        # dp[i][c] max profit for the first i items with capcacity c
        dp  = [[0] * (capacity + 1) for _ in range(len(profit) + 1)]  # or len(weight)

        # Go Over Items
        for i in range(1, len(profit) + 1):
            for c in range(1, capacity + 1):
                # Take Item
                take = -float('inf')
                if weight[i - 1] <= c:
                    take = dp[i-1][c-weight[i - 1]] + profit[i - 1]
                # Skip Item
                skip = dp[i-1][c]
                dp[i][c] = max(take, skip)

        return dp[len(profit)][capacity]