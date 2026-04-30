class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # dp[i] = number of ways to decode suffix s[i:].
        # Invariant: dp[i] is correct after we've computed positions > i.
        dp = [0] * (n + 1)

        # Base: empty suffix has exactly 1 decoding (do nothing).
        dp[n] = 1

        # Build from right to left so dp[i+1], dp[i+2] already known.
        for i in range(n - 1, -1, -1):
            if s[i] == "0":
                # Edge case: no letter maps to "0" alone.
                dp[i] = 0
                continue

            # Option 1: take 1 digit (always valid here since s[i] != '0')
            dp[i] = dp[i + 1]

            # Option 2: take 2 digits if it's a valid code 10..26
            if i + 1 < n and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]

        return dp[0]
