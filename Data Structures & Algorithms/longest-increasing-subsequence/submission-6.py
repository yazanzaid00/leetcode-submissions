class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i][j] = maximum subarray length in nums[i...j] that is strictly increasing 
        dp = [[0 for _ in nums] for _ in nums]
        for i in range(len(nums)):
            dp[i][i] = 1

        # for cur_len in range(2, len(nums)):
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                # 
                dp[i][j] = 1 + max(
                    (dp[k][j] for k in range(i + 1, j + 1) if nums[k] > nums[i]),default=0
                )
                

        return max(
            dp[i][len(nums) - 1] for i in range(len(nums))
        )