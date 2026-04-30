class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = maximum length of LIS such that it ends at index i.
        dp = [1] * len(nums)
        # [9,1,4,2,3,3,7]

        for i in range(1, len(nums)):
            dp[i] = 1 + max(
                (dp[k] for k in range(i) if nums[k] < nums[i]), default = 0
            )

        return max(dp)
