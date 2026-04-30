class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        sList = list(s.lower())
        while (left < right):
            while(not sList[left].isalnum() and left < len(s) - 1):
                left += 1    
            while(not sList[right].isalnum() and right > 0):
                right -= 1    
            if left < right and sList[left] != sList[right]:
                return False
            left += 1
            right -= 1
        return True