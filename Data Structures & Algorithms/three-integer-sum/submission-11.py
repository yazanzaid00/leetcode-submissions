class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        i = 0
        while i < len(nums):
            j, k = i + 1, len(nums) - 1
            while j < k:
                curr_sum = nums[i] + nums[j] + nums[k]
                if curr_sum == 0:
                    # we are done
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                    while i < len(nums) - 1 and nums[i + 1] == nums[i]:
                        i += 1
                elif curr_sum < 0:
                    j += 1

                else:
                    k -= 1

            i += 1
        return res