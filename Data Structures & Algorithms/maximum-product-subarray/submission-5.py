class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        prefix = 0
        suffix = 0
        n = len(nums)

        for i in range(n):
            # reset after zero using (prod or 1)
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)
            res = max(res, prefix, suffix)

        return res
