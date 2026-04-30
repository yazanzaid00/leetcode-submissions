from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # STEP 0: Handle trivial edge cases
        # Q: In which cases is it impossible or trivial to have a valid window?
        if not t or not s or len(t) > len(s):
            return ""

        # STEP 1: Build frequency map for t
        # countT[c] = how many times char c MUST appear in a valid window
        # TODO: use Counter(t) or fill manually in a loop
        countT = Counter(t)   # TODO: if you want, re-implement Counter(t) by hand

        # STEP 2: Initialize sliding-window bookkeeping
        window = {}                   # current window frequencies
        have = 0                      # how many distinct chars currently satisfied
        need = len(countT)            # how many distinct chars must be satisfied in total

        # We'll track best window [resL, resR] and its length
        resL = 0
        resLen = float("inf")

        # Left pointer of the window
        l = 0

        # STEP 3: Expand the window with right pointer r
        for r, c in enumerate(s):
            # 3a) Add s[r] into window
            window[c] = window.get(c, 0) + 1

            # 3b) IMPORTANT CHECK:
            # If c is a required char AND its count just reached exactly the required amount,
            # we just satisfied one more distinct requirement.
            if c in countT and window[c] == countT[c]:
                # TODO: what should we do with 'have' here? Why only when '=='?
                have += 1

            # 3c) While the window is "valid" (covers all requirements), try to shrink from the left
            #     Q: how do we know the window is valid using 'have' and 'need'?
            while have == need:
                # At this point, s[l..r] contains all required chars with correct multiplicities.

                # TODO: compute current length of window (careful with +1)
                cur_len = r - l + 1   # why +1?

                # If this window is smaller than the best so far, update result
                if cur_len < resLen:
                    resLen = cur_len
                    resL = l

                # 3d) Shrink from the left: remove s[l] from the window
                left_char = s[l]
                window[left_char] -= 1

                # If we removed a required char and its count DROPPED BELOW required,
                # this window is no longer valid for that char -> 'have' must go down by 1.
                if left_char in countT and window[left_char] < countT[left_char]:
                    # TODO: what should we do with 'have' here and why?
                    have -= 1

                # Move left boundary rightward
                l += 1

        # STEP 4: Build the answer from resL and resLen
        # If we never updated resLen, there was no valid window.
        if resLen == float("inf"):
            return ""

        # TODO: slice s using resL and resLen (be precise with indices)
        # Q: what is the right-most index we want? Is it inclusive or exclusive in Python slicing?
        return s[resL : resL + resLen]
