class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            numbers[i] -= 0.5 * target
        
        # we want to find if there is a number (x) and its negative value (-x) in the numbers array
        left, right = 0, n - 1

        while (left < right):
            if (numbers[left] == -numbers[right]):
                return [left + 1, right + 1]
            if numbers[right] + numbers[left] < 0:
                left += 1
            else:
                right -= 1
        return None
