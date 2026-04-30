class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i: int) -> int:
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            odd_left = left
            odd_len = right - left + 1
            left, right = i, i + 1
            even_len = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            left += 1
            right -= 1
            even_left = left
            even_len = right - left + 1
            left = even_left if odd_len <= even_len else odd_left
            curr_len = max(odd_len, even_len)
            return (left, curr_len)

        max_left, max_len = 0, 0
        for i in range(len(s)):
            cur_left, cur_len = expand(i)
            if cur_len > max_len:
                max_len = cur_len
                max_left = cur_left
        return s[max_left:max_left + max_len]

