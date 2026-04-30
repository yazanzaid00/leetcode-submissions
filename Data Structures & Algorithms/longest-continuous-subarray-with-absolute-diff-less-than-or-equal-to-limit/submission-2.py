class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_q = deque() # min_q[0] is minimum, keep it non decreasing min_q[i] <= min_q[i + 1]
        max_q = deque() #max_q[0] is maximum, keep it non increasing max_q[i] >= max_q[i + 1]
        l = 0
        max_len = 0
        for r in range(len(nums)):
            # fix queues
            # drop worse candidate
            while min_q and nums[min_q[-1]] >= nums[r]:
                min_q.pop()
            
            while max_q and nums[max_q[-1]] <= nums[r]:
                max_q.pop()
            # consume r
            min_q.append(r)
            max_q.append(r)
            # fix invariant
            if nums[max_q[0]] - nums[min_q[0]] > limit:
                # we need to drop things based on age...
                while min_q and min_q[0] <= l:
                    min_q.popleft()
                while max_q and max_q[0] <= l:
                    max_q.popleft()
                l += 1
            else:
                max_len = max(max_len, r - l + 1)
        return max_len