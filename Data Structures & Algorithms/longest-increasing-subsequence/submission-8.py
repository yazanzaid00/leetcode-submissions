class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] = maximum length of LIS such that it ends at index i.
        dp = [(1, -1)] * len(nums)
        # [9,1,4,2,3,3,7]
        for i in range(1, len(nums)):
            best = 1
            best_ind = i
            for k in range(i):
                if nums[k] < nums[i]:
                    cand = dp[k][0] + 1
                    if cand > best:
                        best = cand
                        best_ind = k
            dp[i] = best, best_ind
        return max(dp, key=lambda x:x[0])[0]
