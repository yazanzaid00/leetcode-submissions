class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permute_helper(start_ind):
            if start_ind == len(nums):
                nonlocal res
                res.append(nums.copy())
                return
            for i in range(start_ind, len(nums)):
                # pick nums[i]
                nums[start_ind], nums[i] = nums[i], nums[start_ind]
                permute_helper(start_ind + 1)
                #undo choice
                nums[start_ind], nums[i] = nums[i], nums[start_ind]
        res = []
        permute_helper(0)
        return res