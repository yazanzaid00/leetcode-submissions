class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] == number of ways to decode s[i:len(s)]== s[i...len(s) - 1]
        dp = [0] * (len(s) + 1)
        # What is the number of ways to decode empty string?
        dp[len(s)] = 1
        #
        # "1012"
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0

            elif i < len(s) - 1 and 10 <= int(s[i:i+2]) <= 26:
                    dp[i] = dp[i + 1] + dp[i + 2]

            else:
                dp[i] = dp[i + 1]
        
        return dp[0]