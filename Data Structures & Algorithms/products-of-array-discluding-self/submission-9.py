class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix[i] the multiplication results of nums[0...i) x
        prefix = [1] * len(nums)
        # suffix[i] the multiplication results of nums (i...len(nums)-1] x
        suffix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        return res