class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        max_price = 0
        buy = prices[0]
        for sell in prices:
            max_price = max(sell - buy, max_price)
            if sell < buy:
                buy = sell
        return max_price