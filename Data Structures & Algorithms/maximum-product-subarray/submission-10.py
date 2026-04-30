class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = 1
        current_min = 1
        global_max = -float("inf")
        for num in nums:
            current_max, current_min = max(current_max * num, num, current_min * num), min(current_max * num, num, current_min * num)
            global_max = max(current_max, global_max)
        return global_max
