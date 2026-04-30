class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        if k == 1:
            return nums[:]
        # monotonic queue/stack we want queue[0] to be the index of maximum at current window so we want it decreasing by the value of the element not the index it self (it will naturaly be also the index as we are moving from left to right, but this is the general idea of monotonic)...
        queue = deque([0])
        res = []
        l = 0
        for r in range(1, len(nums)):
            # consume nums[r], if it is a good candidate consume it...
            # pop worse candidate
            # we pop right because of more recent...
            while queue and nums[r] >= nums[queue[-1]]:
                queue.pop()
            # consume right edge
            queue.append(r)
            # window size is bigger than k, shrink it...
            while r - l + 1 > k:
                # we pop left because of age
                while queue and queue[0] <= l:
                    queue.popleft()
                l += 1
            # append to res
            if r - l + 1 == k:
                res.append(nums[queue[0]])
            
        return res
                
            