class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_str = ''.join(str(digit) for digit in digits)
        number = int(digits_str)
        number += 1
        new_digits = []
        while number > 0:
            new_digits.append(number % 10)
            number //= 10
        new_digits.reverse()
        return new_digits