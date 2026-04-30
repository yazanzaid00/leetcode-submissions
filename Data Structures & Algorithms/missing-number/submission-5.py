class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numsSum = sum(nums)
        expSum = len(nums)*(len(nums)+1) / 2
        return int(expSum) - numsSum