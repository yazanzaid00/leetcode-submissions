class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # sliding window
        l, r, i = 0, 0, 0
        while r < len(haystack):
            if haystack[r] == needle[i]:
                if i == len(needle) - 1:
                    return l
                r += 1
                i += 1
            else:
                l += 1
                r = l
                i = 0
        return -1