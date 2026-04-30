class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] the string is break up unitl index i - 1
        # what if i need to try out another word?
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True # empty string
        i = 0
        while i <= len(s):
            for word in wordDict:
                # i want to try all words in the dictionary and flag all possible indexes of their corresponding length from index i...
                # I can also check == word instead of membership checking...
                # How can I backtrack to try the next word in DP for loop? i want to try the next word in the word dict...
                if dp[i] and i + len(word) <= len(s) and s[i : i + len(word)] == word:
                    dp[i+len(word)] = True
            i += 1
        return dp[len(s)]