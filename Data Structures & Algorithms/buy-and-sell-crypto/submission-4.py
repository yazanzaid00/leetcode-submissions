class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = prices[0]
        # move forward prices
        for sell in prices:
            max_profit = max(max_profit, sell - buy)
            buy = min(buy, sell)

        return max_profit