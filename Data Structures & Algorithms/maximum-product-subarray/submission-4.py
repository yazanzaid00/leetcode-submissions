class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp[i] = maximum product of a subarray that uses index i nums[0...i]...
        dp = [0] * len(nums)
        # dp_2[i] = minimum product of a subarray that uses index i nums[0...i]...
        dp_2 = [0] * len(nums)
        dp[0] = nums[0]
        dp_2[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(
                dp[i - 1] * nums[i],
                dp_2[i - 1] * nums[i],
                nums[i]
            )
            dp_2[i] = min(
                dp_2[i - 1] * nums[i],
                dp[i - 1] * nums[i],
                nums[i]
            )
        return max(dp)