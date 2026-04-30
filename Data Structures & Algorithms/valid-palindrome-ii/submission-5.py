class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(start_index: int, end_index: int) -> bool:
            while start_index < end_index:
                if s[start_index].lower() != s[end_index].lower():
                    return False
                start_index += 1
                end_index -= 1

            return True
        # s is alnum?
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                # delete left character, delete right character
                return isPalindrome(l+1, r) or isPalindrome(l, r - 1)
            # abbda "bb"
            # abkbda -> abkba "bkb"
            l += 1
            r -= 1

        return True