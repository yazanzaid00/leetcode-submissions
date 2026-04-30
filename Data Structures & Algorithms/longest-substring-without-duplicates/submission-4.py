class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_len = 0
        l = 0
        # expand window
        for r in range(len(s)):
            while s[r] in seen:
                # shrink window
                seen.remove(s[l]) # pop or remove for set?
                l += 1
            seen.add(s[r])
            # invariant holds s[l...r] is non repeating... we can proceed with this:
            max_len = max(max_len, r - l + 1)
        return max_len
            