# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         sDict = dict()
#         for char in s:
#             if char in sDict:
#                 sDict.update({char: sDict.get(char)+1})
#             else:
#                 sDict.update({char: 1})
#         flagLength = len(s)
#         for char in t:
#             if char in sDict:
#                 sDict.update({char: sDict.get(char)-1})
#                 flagLength -= 1
#                 if (sDict.get(char) < 0):
#                     return False
#             else:
#                 return False
#         return flagLength == 0
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):           # early exit
            return False
        counts = {}
        for ch in t:
            counts[ch] = counts.get(ch, 0) + 1
        for ch in s:
            if ch not in counts:
                return False
            counts[ch] -= 1
            if counts[ch] < 0:
                return False
        return True