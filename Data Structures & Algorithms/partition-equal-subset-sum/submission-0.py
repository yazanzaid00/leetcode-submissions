class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # two pointers
        def part_helper(subset1, subset2, curr_i):
            if curr_i == len(nums):
                return subset1 == subset2
            # take num in subset1, or in subset2
            if part_helper(subset1 + nums[curr_i], subset2, curr_i + 1) or part_helper(subset1, subset2 + nums[curr_i], curr_i + 1):
                return True

        subset1, subset2 = 0, 0
        # take num in subset1, or in subset2
        if part_helper(subset1 + nums[0], subset2, 1) or part_helper(subset1, subset2 + nums[0], 1):
            return True

        return False
