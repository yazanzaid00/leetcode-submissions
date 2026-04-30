class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, max_len = 0, 0
        hash_table = defaultdict(int) 
        for r in range(len(s)):
            # expand sliding window
            hash_table[s[r]] += 1
            max_freq = max(hash_table.values())
            curr_len = r - l + 1
            # shrink sliding window
            # While invalid condition
            while l < len(s) and curr_len - max_freq > k:
                #shrink window
                hash_table[s[l]] -= 1
                l += 1
                curr_len = r - l + 1
                max_freq = max(hash_table.values())
            max_len = max(max_len, curr_len)
        return max_len