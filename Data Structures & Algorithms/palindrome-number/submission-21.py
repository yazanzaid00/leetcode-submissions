class Solution:
    def isPalindrome(self, x: int) -> bool:
        if 0 <= x <= 9:
            return True
        if x < 0 or x % 10 == 0 :
            return False
        x_mirror = 0
        # 121
        while x > x_mirror:
            x_mirror = x_mirror * 10 + x % 10 #
            x //= 10 # 
        
        return x_mirror//10 == x or x == x_mirror
        