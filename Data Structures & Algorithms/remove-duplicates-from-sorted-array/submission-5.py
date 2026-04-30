class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueCount = 0
        for i in range(len(nums)):
            uniqueCount += 1
            while(i < len(nums) - 1 and nums[i] == nums[i+1]):
                print(f"deleted {nums[i+1]}")
                nums.pop(i+1)
        return uniqueCount