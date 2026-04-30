class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] = True iff s[0...i - 1] breakable (i can use word dicts to break it)
        dp = [False] * (len(s) + 1)
        # s[0... -1] מחרוזת ריקה 
        dp[0] = True
        for i in range(1, len(s) + 1):
            # s[0...i - 1] breakable (i can use word dicts to break it)
            # s[0...i - 2], s[0...i - 3], s[0...i - 4],.... s[0...-1]    
            # if s[0... i - 2] breakable
            # dp[i] = dp[i - 1] and i-1 i-1 + len(word)
            if not dp[i - 1]:
                continue
            
            for word in wordDict:
                if i - 1 + len(word) <= len(s) and s[i - 1:i - 1 +len(word)] == word:
                    dp[i - 1 + len(word)] = True
        # dp[i] = True iff s[0...i - 1] breakable (i can use word dicts to break it)
        return dp[len(s)]