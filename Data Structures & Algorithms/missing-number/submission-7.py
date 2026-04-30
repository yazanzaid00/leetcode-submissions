from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        cum_xor = len(nums)
        for i in range(len(nums)):
            cum_xor ^= i ^ nums[i]
        return cum_xor
