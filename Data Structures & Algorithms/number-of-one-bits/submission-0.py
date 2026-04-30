class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(digit == "1" for digit in bin(n))
        

