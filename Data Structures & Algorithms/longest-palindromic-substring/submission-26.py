class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i: int):
            # odd length palindrome
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # left += 1
            max_left, max_right = left + 1, right
            if i + 1 >= len(s):
                return max_left, max_right
            # even length palindrome
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            if right - left > max_right - max_left:
                max_left, max_right = left, right
            return max_left, max_right
        
        max_left, max_right = 0, 1
        for i in range(len(s)):
            left, right = expand(i)
            if right - left > max_right - max_left:
                max_left, max_right = left, right
        return s[max_left: max_right]