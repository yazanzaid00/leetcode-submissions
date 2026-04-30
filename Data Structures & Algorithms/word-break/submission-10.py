from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = {}  # memo: start -> bool

        def wordHelper(start=0):
            n = len(s)
            if start in dp:              # reuse result for this suffix
                return dp[start]
            if start == n:               # consumed the whole string
                return True

            # try all ends after start
            for end in range(start + 1, n + 1):
                if s[start:end] in wordSet and wordHelper(end):
                    dp[start] = True
                    return True

            dp[start] = False
            return False

        return wordHelper(0)