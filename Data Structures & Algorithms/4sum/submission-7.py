from collections import defaultdict
from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # sort so we can move over it...
        nums.sort()
        def kSum(k, new_target, res, quad, start_index):
            # base case 2sum
            if k == 2:
                left, right = start_index, len(nums) - 1
                while left < right:
                    curr_sum = nums[left] + nums[right]
                    # we found our sum
                    if curr_sum == new_target:
                        # we need to insert the full Quadraplet
                      
                        res.append(quad + [nums[left], nums[right]])
                        # skip duplicates
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        # skip duplicate
                        right -= 1 
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif curr_sum > new_target:
                        right -= 1
                    elif curr_sum < new_target:
                        left += 1
            # $ recursive case k > 2 such as k = 3
            else:
                while start_index < len(nums):
                    # we take nums[start_index]
                    kSum(k - 1, new_target - nums[start_index], res,  quad + [nums[start_index]], start_index + 1)
                    # we pop to try next combinations
                    # quad.pop() # guarantee dlast elemnt...
                    # we need to skip similar numbers, we can use bisect, we can do while loop...
                    start_index += 1
                    while start_index < len(nums) and nums[start_index - 1] == nums[start_index]:
                        start_index += 1
        res = []
        kSum(4, target, res, [], 0)
        return res

            