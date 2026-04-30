class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return None
        if len(nums) <= 1:
            return nums[0]
        dp = [None] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        # dp[i] shows the maximum value up until house i
        for i in range(2, len(nums)):
            
            dp[i] = max(
                # take the house i
                nums[i] + dp[i - 2],
                #don't take the house i
                dp[i - 1]
            )
        return dp[len(nums) - 1]
            