class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0 # first day
        sell = 1 # second day
        # day is moving forward
        for sell in range(1, len(prices)):
            max_profit = max(max_profit, prices[sell]-prices[buy])
            if prices[buy] > prices[sell]:
                buy = sell
        return max_profit
            
