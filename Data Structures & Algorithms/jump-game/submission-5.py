class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums)
        if not nums or target <= 1:
            return True
        dp = [False] * target
        dp[0] = True
        dp[1] = bool(1 <= nums[0])
        # dp[i] can it reach from index 0 to index i?
        for i in range(2, target):
            for j in range(i):
                if dp[j] and i - j <= nums[j]:
                    dp[i] = True
                    break

        return dp[target - 1]