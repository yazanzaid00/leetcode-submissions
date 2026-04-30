class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cum_xor = nums[0] ^ 0
        for i in range(1, len(nums)):
            cum_xor ^= nums[i] # nums
            cum_xor ^= i
        cum_xor ^= len(nums)
        return cum_xor
