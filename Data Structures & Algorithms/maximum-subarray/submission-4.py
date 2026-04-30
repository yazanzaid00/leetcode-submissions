class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # of up until now sum is positive continue, otherwise don't start from this index...
        # max_sum(i + 1) = max(max_sum(i) +nums[i], nums[i])
        global_max = prev = nums[0] # base case
        for i in range(1, len(nums)):
            prev = max(prev + nums[i], nums[i] )
            global_max = max(global_max, prev)
        return global_max