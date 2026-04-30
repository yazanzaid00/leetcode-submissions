class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s: str) -> bool:
            l, r = 0, len(s) - 1
            while l < r:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1

            return True
        # s is alnum?
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # delete left character, delete right character
                return isPalindrome(s[l+1:r+1]) or isPalindrome(s[l:r])
            # abbda "bb"
            # abkbda -> abkba "bkb"
            l += 1
            r -= 1

        return True