class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        length = len(s)
        dp = [False]*length
        for i in range(length):
            for j in range(-1,i):
                if s[j+1:i+1] in wordSet and (j == -1 or dp[j]):
                    dp[i] = True
                    break
        return dp[length-1]