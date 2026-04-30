class Solution:
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        def twoSum(target, res_array=result, start=0,):
            end = len(nums) - 1
            while (start < end):
                curr_sum = nums[start] + nums[end] + target
                if curr_sum > 0:
                    end -= 1
                elif curr_sum < 0:
                    start += 1
                else:
                    res_array.append((nums[start], nums[end], target))
                    start += 1
                    while (start < end and nums[start - 1] == nums[start]):
                        start += 1
        
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            twoSum(start = i + 1, target=nums[i], res_array=result)
            i += 1
            while (i < len(nums) and nums[i] == nums[i - 1]):
                i += 1
        
        return result
        
