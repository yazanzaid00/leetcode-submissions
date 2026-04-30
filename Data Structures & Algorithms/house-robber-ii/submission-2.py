class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # dp_0[i] = maximum value for first i items excluding last item...
        dp_0 = [0] * (len(nums) + 1)
        dp_0[1] = nums[0]
        for i in range(2, len(nums)):
            dp_0[i] = max(
                dp_0[i - 1],
                dp_0[i - 2] + nums[i - 1]
            )
        
        # dp_1[i] = maximum value for i items excluding 0... dp_1[i] = nums[1...i]
        dp_1 = [0] * (len(nums) + 1)
        dp_1[1] = nums[1]
        for i in range(2, len(nums)):
            dp_1[i] = max(
                dp_1[i - 1],
                dp_1[i - 2] + nums[i]
            )
        return max(
            dp_0[len(nums) - 1],
            dp_1[len(nums) - 1],
        )