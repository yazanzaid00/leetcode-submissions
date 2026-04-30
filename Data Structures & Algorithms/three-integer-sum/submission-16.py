class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def two_sum(chosen_ind):
            nonlocal res
            l, r = chosen_ind + 1, len(nums) - 1
            while l < r:
                cur_sum = nums[l] + nums[r] + nums[chosen_ind]
                if cur_sum == 0:
                    res.append([nums[chosen_ind], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif cur_sum < 0:
                    l += 1
                else:
                    r -= 1
        res = []
        i = 0
        while i < len(nums) - 2:
            # 1 1 1 2
            while 0 < i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
            two_sum(i)
            i += 1
        return res
