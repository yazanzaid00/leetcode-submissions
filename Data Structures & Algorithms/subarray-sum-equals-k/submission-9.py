class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prev_sums = defaultdict(int)
        prev_sums[0] = 1
        count = 0
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum - k in prev_sums:
                count += prev_sums.get(curr_sum - k)
            prev_sums[curr_sum] += 1
        return count
            