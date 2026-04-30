class Solution:
    def numDecodings(self, s: str) -> int:
        # dp[i] == number of ways to decode s[i:len(s)]== s[i...len(s) - 1]
        # dp = [0] * (len(s) + 1)
        # What is the number of ways to decode empty string?
        dp1 = 1
        dp2 = 0
        temp = 0
        # "1012"
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                temp = 0

            elif i < len(s) - 1 and 10 <= int(s[i:i+2]) <= 26:
                    temp = dp1 + dp2

            else:
                temp = dp1
            
            dp1, dp2 = temp, dp1
        
        return dp1