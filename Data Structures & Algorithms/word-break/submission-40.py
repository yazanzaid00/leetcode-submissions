class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] = substring s[0...i) = s[0...i-1] is breakable
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            if not dp[i]:
                continue
            for word in wordDict:
                if i + len(word) <= len(s) and s.startswith(word, i, i + len(word)):
                    dp[i + len(word)] = True

        return dp[len(s)]