class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sums[nums[i]+nums[j]].append([i, j])
        
        if target in sums:
            return sums[target][0]

