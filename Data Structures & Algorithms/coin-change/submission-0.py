class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] the minimal number of coins to have i money
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            if coin < amount + 1:
                dp[coin] = 1
        for money in range(amount + 1):
            for coin in coins:
                if 0 <= money - coin <= amount:
                    dp[money] = min(
                        dp[money],
                        dp[money - coin] + 1
                    )
        return -1 if dp[amount] == float('inf') else dp[amount]