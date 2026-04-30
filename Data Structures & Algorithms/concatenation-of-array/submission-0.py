class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = [] # of size 2n
        for num in nums:
            result.append(num)
        for num in nums:
            result.append(num)

        return result