class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = defaultdict(list)
        for index, num in enumerate(nums):
            sums[target-num].append(index)
        
        for i, num in enumerate(nums):
            indices = sums.get(num)
            if indices:
                for j in indices:
                    if i != j:
                        return [i, j]

        return False
