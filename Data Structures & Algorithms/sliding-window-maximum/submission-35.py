class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # we can solve this using max heap of size k
        # different approach is using mononic queue
        queue = deque() # monotonic queue where queue[0] is the maximum value, and it is non-increasing s.t. queue[0] < queue[1]... < queuep[len(queu-1)]
        res = []
        l = 0
        for r in range(len(nums)):
            # do something
            # fix size invariant
            # i need to consume r always...
            # expand window
            while queue and nums[r] >= nums[queue[-1]]:
                # we found better more recent candidate pop it...
                queue.pop()
            queue.append(r)
            # shrink window
            if r - l + 1 > k:
                l += 1
            # pop elements that are aged well
            while queue and queue[0] < l:
                queue.popleft()
            if queue and r - l + 1 == k:
                res.append(nums[queue[0]])
        return res