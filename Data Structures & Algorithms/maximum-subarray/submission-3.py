class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # of up until now sum is positive continue, otherwise don't start from this index...
        # max_sum(i + 1) = max(max_sum(i) +nums[i], nums[i])
        max_sum = [0]*len(nums)
        global_max = max_sum[0] = nums[0] # base case
        for i in range(1, len(nums)):
            max_sum[i] = max(
                max_sum[i - 1] + nums[i],
                nums[i]
            )
            global_max = max(global_max, max_sum[i])
        return global_max