class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums)
        if not nums or length <= 1:
            return True
        max_index_reach = 0 + nums[0]
        for i in range(1, length):
            # if i reachable:
            if i <= max_index_reach:
                max_index_reach = max(i+ nums[i], max_index_reach)
        return max_index_reach >= length - 1
