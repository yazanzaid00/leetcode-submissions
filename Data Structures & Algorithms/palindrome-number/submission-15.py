class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x > 0):
            return False
        if x <= 9:
            return True
        
        x_mirror = 0
        x_remaining = x # 121
        # 121
        while x_remaining > x_mirror:
            x_mirror *= 10 #
            x_mirror += x_remaining % 10 #
            x_remaining //= 10 # 
        
        return x_mirror//10 == x_remaining or x_remaining == x_mirror
        