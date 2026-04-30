class MedianFinder:

    def __init__(self):
        self.min_heap = [] # save the bigger than median
        self.max_heap = [] # save the smaller than median
        self.median = None
    def addNum(self, num: int) -> None:
        self.median = num if self.median is None else self.findMedian()
        if num <= self.median:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        # fix heaps
        if len(self.min_heap) - len(self.max_heap) > 1:
            # self.min heap is bigger
            min_val = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -min_val)
        elif len(self.max_heap) - len(self.min_heap) > 1:
            min_val = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -min_val)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return -self.max_heap[0]