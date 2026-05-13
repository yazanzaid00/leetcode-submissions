class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        max_len = 0
        seen = set()
        for r in range(len(s)):
            # decrease window size if it was seen before 
            while s[r] in seen and l < r:
                # how to remove in set?
                seen.remove(s[l])
                l += 1
            # then calc the max_len window size accordingly
            seen.add(s[r])
            max_len = max(max_len, r - l + 1)

        return max_len
