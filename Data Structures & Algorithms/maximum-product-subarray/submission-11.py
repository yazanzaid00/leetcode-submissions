class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # max_dp[i] = max subarray that use the element i - 1 elements
        # min_dp[i] = min subarray that use the element i - 1 elements
        max_dp = [-float("inf") ] * len(nums)
        min_dp = [float("inf") ] * len(nums)
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        for i in range(1, len(nums)):
            max_dp[i] = max(
                nums[i],
                max_dp[i - 1] * nums[i],
                min_dp[i - 1] * nums[i]
            )
            min_dp[i] = min(
                nums[i],
                max_dp[i - 1] * nums[i],
                min_dp[i - 1] * nums[i]
            )
        return max(max_dp)