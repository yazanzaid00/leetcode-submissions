class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        jump_nums = 0
        while r < len(nums) - 1:
            farthest = r
            for i in range(l, r + 1):
                farthest = max(farthest, i+nums[i])
            l = r + 1
            r = farthest

            jump_nums += 1
        return jump_nums