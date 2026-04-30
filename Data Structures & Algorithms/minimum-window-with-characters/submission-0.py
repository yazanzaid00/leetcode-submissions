class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def s_in_t(s_counter, t_counter):
            for char in t:
                if char not in s_counter or s_counter[char] < t_counter[char]:
                    return False
            return True
        t_counter = defaultdict(int)
        s_counter = defaultdict(int)
        for char in t:
            t_counter[char] += 1
        l = 0
        min_len = float('inf')
        for r in range(len(s)):
            # consume s[r]
            s_counter[s[r]] += 1
            while l <= r and s_in_t(s_counter, t_counter):
                cur_len = r - l + 1
                if cur_len < min_len:
                    min_len = cur_len
                    start = l
                s_counter[s[l]] -= 1
                if s_counter[s[l]] == 0:
                    del s_counter[s[l]]
                l += 1
        return "" if min_len == float("inf") else s[start:start+min_len] 