class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        buy = 0 # first day
        sell = 1 # second day
        for day in range(1, len(prices)):
            max_profit = max(prices[sell]-prices[buy], max_profit)
            # Update better options, for sell it is ok to update to the latest
            if prices[day] > prices[sell]:
                sell = day
                max_profit = max(prices[sell]-prices[buy], max_profit)
            elif prices[day] < prices[buy]:
                buy = day
                if sell < buy:
                    sell = buy + 1

        return max_profit
            
