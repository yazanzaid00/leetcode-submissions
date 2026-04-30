class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        buy = 0
        max_profit = 0
        for sell in range(1, len(prices)):
            max_profit = max(max_profit, prices[sell] - prices[buy])
            if prices[sell] < prices[buy]:
                buy = sell
        return max_profit