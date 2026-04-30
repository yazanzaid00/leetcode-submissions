class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        # Look at Two Characters each time
        for i in range(len(s)):
            if('a' > s[i] or s[i] > 'z'):
                # throw error
                raise ValueError("not lower characters")
            j = min(i+1, len(s)-1)
            score += abs((ord(s[i]))-ord(s[j]))
        return score