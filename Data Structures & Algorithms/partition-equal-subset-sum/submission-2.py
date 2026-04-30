class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        # dp[s] == True ⇔ there exists a subset with sum s
        dp = [False] * (target + 1)
        dp[0] = True  # empty subset forms sum 0

        for num in nums:
            # Iterate backwards to avoid reusing the same num multiple times
            for s in range(target, num - 1, -1):
                if dp[s - num]:
                    dp[s] = True

        return dp[target]
