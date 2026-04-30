class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq_nums = set()
        for num in nums:
            uniq_nums.add(num)
        max_len = 0
        for num in uniq_nums:
            i = 1
            while num + i in uniq_nums:
                i += 1
            max_len = max(i, max_len)
        return max_len