from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        max_stack = deque()  # stores indices, values decreasing
        l = 0

        for r in range(len(nums)):
            # 1) Pop from BACK while current value is >= last value
            #    -> maintain decreasing nums[max_stack[0]] >= ... >= nums[max_stack[-1]]
            while max_stack and nums[max_stack[-1]] <= nums[r]:
                max_stack.pop()

            # 2) Add current index to the deque
            max_stack.append(r)

            # 3) Remove from FRONT if index is left of the window [l, r]
            if max_stack[0] < l:
                max_stack.popleft()

            # 4) When window has size k, record max and slide l
            if r - l + 1 == k:
                res.append(nums[max_stack[0]])
                l += 1   # slide window: remove nums[l] from window next round if needed

        return res
