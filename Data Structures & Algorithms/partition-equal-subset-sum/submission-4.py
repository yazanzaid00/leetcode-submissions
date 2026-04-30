class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)
        if nums_sum % 2:
            return False
        nums_sum //= 2
        dp = [[False] * (nums_sum + 1) for _ in range(len(nums) + 1)]
        dp[0][0] = True # empty subset
        # dp[i][j] == True if considering the first i items, we have a subset of sum = j
        for i in range(1, len(nums) + 1):
            for j in range(nums_sum + 1):
                # skip nums[i]
                dp[i][j] = dp[i - 1][j]
                # take nums[i]
                if 0 <= j - nums[i - 1] <= nums_sum:
                    dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i][j]

        return dp[len(nums)][nums_sum]