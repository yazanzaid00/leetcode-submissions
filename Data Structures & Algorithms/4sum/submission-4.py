from collections import defaultdict
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        nums.sort()
        a = 0
        while a < len(nums):
            # 2 2 2 2
            b = a + 1
            while b < len(nums):
                left, right = b + 1, len(nums) - 1
                while left < right:
                    curr_sum = nums[a] + nums[b] + nums[left] + nums[right]
                    if curr_sum == target:
                        res.append([nums[a], nums[b], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    if curr_sum < target:
                        left += 1
                    if curr_sum > target:
                        right -= 1
                while b < len(nums) - 1 and nums[b] == nums[b + 1]:
                    b += 1
                b += 1
            while a < len(nums) - 1 and nums[a] == nums[a + 1]:
                    a += 1
            a += 1
        return res

