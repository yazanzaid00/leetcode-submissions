class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(l, r):
            nonlocal best_len, best_start
            cur_start, cur_len = 0, 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cur_start = l
                cur_len = r - l + 1
                l -= 1
                r += 1
            if cur_len > best_len:
                best_start = cur_start
                best_len = cur_len

        best_start, best_len = 0, 0
        for l in range(len(s)):
            # odd
            expand(l, l)
            # even
            expand(l, l + 1)

        return s[best_start:best_start+best_len]