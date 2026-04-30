class Solution:
    def longestPalindrome(self, s: str) -> str:
        # self expanding DP? 
        # DP[i] = longest palindorme where the center is i... it stopped becoming DP problem... there is no recursive, can it be solved using DP?
        def longest_palindrome(start_index):
            global_max = curr_max = [1, (start_index, start_index)] # the letter it self
            # odd case "ccc"
            l, r = start_index - 1, start_index + 1
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    curr_max[0] += 2
                    curr_max[1] = l, r
                else:
                    break
                l -= 1
                r += 1
            # even case
            global_max = max(curr_max, global_max, key=lambda x: x[0])
            if s[start_index - 1] == s[start_index]:
                curr_max = [2, (start_index - 1, start_index)] 
                l, r = start_index - 2, start_index + 1
                while l >= 0 and r < len(s):
                    if s[l] == s[r]:
                        curr_max[0] += 2
                        curr_max[1] = l, r
                    else:
                        break
                    l -= 1
                    r += 1
            global_max = max(curr_max, global_max, key=lambda x: x[0])
            return global_max
        global_max = [1,(0,0)] # base case
        for i in range(1, len(s)):
            curr_max = longest_palindrome(i)
            global_max = max(curr_max, global_max, key=lambda x: x[0])
        
        print(global_max)
        start_index, end_index = global_max[1]
        return s[start_index : end_index + 1]
