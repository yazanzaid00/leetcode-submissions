class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # sliding window
        l, r, i = 0, 0, 0
        while r < len(haystack):
            if haystack[r] == needle[r - l]:
                if r - l == len(needle) - 1:
                    return l
                r += 1
            else:
                l += 1
                r = l
        return -1