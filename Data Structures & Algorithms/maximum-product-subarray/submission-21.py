class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # max_dp[i] = max subarray that use the element i - 1 elements
        # min_dp[i] = min subarray that use the element i - 1 elements
        res = prev = prev_min = nums[0]
        for i in range(1, len(nums)):
            temp_prev = prev
            prev = max(
                nums[i],
                prev * nums[i],
                prev_min * nums[i]
            )

            prev_min = min(
                nums[i],
                temp_prev * nums[i],
                prev_min * nums[i]
            )
            
            res = max(
                res,
                prev
                )
        return res