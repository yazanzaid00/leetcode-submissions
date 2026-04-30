class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        counter = defaultdict(int)
        l = 0
        for r in range(len(s)): 
            # consume r
            counter[s[r]] += 1
            while l < r and sum(counter.values()) - max(counter.values()) > k:
                counter[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest