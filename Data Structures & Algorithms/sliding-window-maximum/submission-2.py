class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap_max = nums[:k:] # window of size k
        heapq.heapify_max(heap_max)
        res = [heap_max[0]]
        for i in range(k, len(nums)):
            # pop the previous item
            heap_max.remove(nums[i - k])
            heapq.heapify_max(heap_max)
            #append the new item
            heapq.heappush_max(heap_max, nums[i])
            res.append(heap_max[0])
            
        return res