class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permute_helper(start_ind, inner_res):
            if len(inner_res) == len(nums):
                nonlocal res
                res.append(inner_res.copy())
            for i in range(start_ind, len(nums)):
                # pick nums[i]
                inner_res.append(nums[i])
                nums[start_ind], nums[i] = nums[i], nums[start_ind]
                permute_helper(start_ind + 1, inner_res)
                #undo choice
                inner_res.pop()
                nums[start_ind], nums[i] = nums[i], nums[start_ind]
        res = []
        permute_helper(0, [])
        return res