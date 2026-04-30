class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_copy = x
        rev = 0
        # 123
        while x_copy > 0:
            # 3
            rev += x_copy % 10
            rev *= 10
            x_copy //= 10
        rev //= 10
        return rev == x