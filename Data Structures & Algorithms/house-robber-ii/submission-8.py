class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        n = len(nums)
        def max_dp(nums):
            # dp[i] max money using the nums[0...i]
            dp = [0] * len(nums)
            prev2 = nums[0]
            prev1 = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                temp_prev1 = prev1
                prev1 = max(
                    prev1,
                    prev2 + nums[i]
                    )
                prev2 = temp_prev1
            return prev1
        return max(max_dp(nums[1:n]), max_dp(nums[0: n - 1]))