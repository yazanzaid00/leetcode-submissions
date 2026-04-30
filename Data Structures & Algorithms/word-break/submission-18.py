class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # we can look at suffix or prefix 
        # let's make dp[i] means if s[0:i] can be broken into valid words
        dp = [False] * (len(s) + 1)
        dp[0] = True
        words = set(wordDict)
        for i in range(len(s)):
            for word in words:
                    if dp[i] and i + len(word) <= len(s) and s[i:i+len(word)] == word:
                        dp[i+len(word)] = True
            
        return dp[-1]