class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        pre_sum = defaultdict(int)
        pre_sum[0] = 1
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            # cur_sum - pre_sum = k
            if cur_sum - k in pre_sum:
                count += pre_sum[cur_sum - k]
            pre_sum[cur_sum] += 1
        return count
            