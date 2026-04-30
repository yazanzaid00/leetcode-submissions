class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            nonlocal max_start, max_length
            curr_start = l
            curr_length = 0
            if l == r:                
                curr_length = 1
                l -= 1
                r += 1
            # odd and even handled the same because we look at two characters at same time
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                curr_start = l
                curr_length = r - l + 1
                l -= 1
                r += 1
            if curr_length > max_length:
                max_start, max_length = curr_start, curr_length
        
        curr_start = 0
        curr_length = 1
        max_start = 0
        max_length = 1
        for i in range(len(s)):
            # odd palindrome
            expand(i, i)
            # even plaindrome
            expand(i, i+1)

        return s[max_start:max_start+max_length]