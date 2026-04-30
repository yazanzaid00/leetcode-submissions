class Solution:
    def isPalindrome(self, x: int) -> bool:
        # we want a systematic way to get the next/previous digit, we can use bitwise mask with 0 on digits we don't want and 1 on digits we want
        # we can get the length of x and base on that to calculate current digit left/right accordingly...
        if x < 0:
            return False
        if 0 <= x <= 9:
            return True
        length = 0
        x_copy = x
        # 321
        while x_copy:
            x_copy //= 10 
            length += 1 # 321 32 3
        # 321
        curr_len = length # 3
        while curr_len > length // 2:
            # 321
            digit_left = (x//10**(curr_len - 1)) % 10  # x/100 == 3 x/10 = 2 x/ 1
            digit_right = (x//10**(length-curr_len)) % 10 # 
            if digit_left != digit_right:
                return False
            curr_len -= 1

        return True
