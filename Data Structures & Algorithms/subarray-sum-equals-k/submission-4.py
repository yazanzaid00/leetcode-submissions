class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_table = defaultdict(int,{0 : 1}) # empty set
        curr_prefix, counter = 0, 0
        for i in range(len(nums)):
            curr_prefix += nums[i]
            counter += prefix_table.get(curr_prefix - k, 0)
            prefix_table[curr_prefix] += 1
        return counter