class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            cur_sum = numbers[l] + numbers[r]
            if target == cur_sum:
                return [l + 1, r + 1]
            elif cur_sum < target:
                l += 1
            else:
                r -= 1
        return [l, r]