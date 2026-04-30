class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dfs = {} # up until key (index, non including) the word is breakable...
        def wordBreakHelper(start_index: int) -> bool:
            # base case
            if start_index == len(s):
                return True

            # memo check first
            if start_index in dfs:
                return dfs[start_index]

            # explore choices
            for word in wordDict:
                if s[start_index:start_index + len(word)] == word:
                    if wordBreakHelper(start_index + len(word)):
                        dfs[start_index] = True
                        return True

            dfs[start_index] = False
            return False


        return wordBreakHelper(0)