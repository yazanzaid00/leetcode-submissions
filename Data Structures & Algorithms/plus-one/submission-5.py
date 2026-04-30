class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 0
        power = 0
        for digit in reversed(digits):
            number += digit * 10 ** power
            power += 1
        number += 1
        return [digit for digit in str(number)]