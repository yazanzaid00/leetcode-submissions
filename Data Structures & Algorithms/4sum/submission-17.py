class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def twoSum(start_ind, two_target, quad):
            nonlocal res
            l, r = start_ind, len(nums) - 1
            while l < r:
                cur_sum = nums[l] + nums[r]
                if cur_sum == two_target:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and  nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and  nums[r] == nums[r + 1]:
                        r -= 1
                elif cur_sum < two_target:
                    l += 1
                else:
                    r -= 1

        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            # deduplicate by taking first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                twoSum(j + 1, target - (nums[i] + nums[j]), [nums[i], nums[j]])
        return res