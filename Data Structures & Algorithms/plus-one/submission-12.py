class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new_digits = []
        carry = 1
        digit_added = -1
        digits_reversed = list(reversed(digits))
        for digit in digits_reversed:
            if digit == 9:
                new_digits.append(0)
                digit_added +=1
            else:
                carry = 0
                new_digits.append(digit + 1)
                digit_added +=1
                break
        if carry == 1:
            new_digits.append(1)
            carry = 0
        else:
            new_digits.extend(digits_reversed[digit_added + 1:])
        new_digits.reverse()
        return new_digits
