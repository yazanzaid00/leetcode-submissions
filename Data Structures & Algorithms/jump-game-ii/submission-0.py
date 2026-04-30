class Solution:
    def jump(self, nums: List[int]) -> int:
        # dp[i] = mininum number of jumps to reach stair number i
        dp = [float('inf')] * len(nums)
        dp[0] = 0
        for i in range(1, len(nums)):
            # I know how to get to all less than < i stairs in minimal steps, so i want to take min(dp[j] + 1 if nums[j] >= i -j)
            for j in range(i):
                if nums[j] >= i - j:
                    dp[i] = min(dp[j] + 1, dp[i])
        return dp[len(nums) - 1]