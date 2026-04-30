class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0
        for day in range(len(prices)):
            max_profit = max(prices[day] - prices[buy], max_profit)
            if prices[day] < prices[buy]:
                buy = day
        return max_profit