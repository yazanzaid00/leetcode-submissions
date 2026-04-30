class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:        
        i, uniqueCounts = 0, 0
        while(i < len(nums)):
            nums[uniqueCounts] = nums[i]
            uniqueCounts += 1
            # similar index
            while(i < len(nums) - 1 and nums[i] == nums[i + 1]):
                i += 1
            i += 1
        return uniqueCounts
                
            


# uniqueCount = 0
        # for i in range(len(nums)):
        #     uniqueCount += 1
        #     while(i < len(nums) - 1 and nums[i] == nums[i+1]):
        #         print(f"deleted {nums[i+1]}")
        #         nums.pop(i+1)
        # return uniqueCount