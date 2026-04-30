class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 1:
            return True

        dp = [False] * n
        dp[0] = True

        # maxReach: farthest index we can reach so far from any reachable index
        maxReach = 0 + nums[0]

        for i in range(1, n):
            # If current index is beyond everything we can reach -> stuck
            if i > maxReach:
                dp[i] = False
            else:
                dp[i] = True
                # update farthest reach if jumping from i extends it
                if i + nums[i] > maxReach:
                    maxReach = i + nums[i]

        return dp[n - 1]
