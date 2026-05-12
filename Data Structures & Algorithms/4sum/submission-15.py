class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(inner_quad, start_ind, two_target):
            nonlocal res
            l, r = start_ind, len(nums) - 1

            while l < r:
                cur_sum = nums[l] + nums[r]

                if cur_sum < two_target:
                    l += 1
                elif cur_sum > two_target:
                    r -= 1
                else:
                    res.append(inner_quad + [nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l < r and nums[l - 1] == nums[l]:
                        l += 1
                    while l < r and nums[r + 1] == nums[r]:
                        r -= 1

        res = []
        nums.sort()

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                twoSum([nums[i], nums[j]], j + 1, target - (nums[i] + nums[j]))

        return res