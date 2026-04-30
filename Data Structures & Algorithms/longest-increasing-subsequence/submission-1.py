class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # let's define dp[i] the longest increasing subsequence of nums[0:i] length that uses index i
        dp = [1] * (len(nums))
        for i in range(len(nums)):
            curr_max = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    curr_max = dp[j] + 1
                dp[i] = max(dp[i], curr_max)
        return max(dp)