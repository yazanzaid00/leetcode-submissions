class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        k_win = deque() # k_win[0] >= k_win[1] >=.... 
        for r in range(len(nums)):
            # remove unnecessary elements from the right to add the new representative
            while k_win and nums[r] > nums[k_win[-1]]:
                k_win.pop()
            k_win.append(r)
            # fix invariant k sized
            # if bigger than size k drop left
            while k_win and r - k_win[0] + 1 > k:
                k_win.popleft()
            if r >= k - 1:
                res.append(nums[k_win[0]])

        return res