class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] = True iff s[0...i - 1] breakable (i can use word dicts to break it)
        dp = [False] * (len(s) + 1)
        # s[0... -1] מחרוזת ריקה 
        dp[0] = True
        for i in range(len(s)):
            if not dp[i]:
                continue
            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                    dp[i + len(word)] = True
        return dp[len(s)]