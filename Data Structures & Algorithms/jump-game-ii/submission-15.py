class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        l, r = 0, 0
        num_jumps = 0
        farthest = 0
        while r < len(nums):
            num_jumps += 1
            farthest = max (j + nums[j] for j in range(l, r + 1))
            if farthest >= len(nums) - 1:
                return num_jumps
            l = r + 1
            r = farthest
        return num_jumps