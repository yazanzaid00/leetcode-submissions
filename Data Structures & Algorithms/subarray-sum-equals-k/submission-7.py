class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        curr_sum, res = 0, 0
        for num in nums:
            curr_sum += num
            # curr_sum - (curr_sum - k) = k where (curr_sum - k) is the old prefix, it coudl be multiple
            res += prefix_sum.get(curr_sum - k, 0) # guaranteed to have
            prefix_sum[curr_sum] += 1
        return res