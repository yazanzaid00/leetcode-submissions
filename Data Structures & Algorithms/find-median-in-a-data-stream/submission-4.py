class MedianFinder:

    def __init__(self):
        self._min_heap = [] # contains the bigger numbers
        self._max_heap = [] # contains the smaller numbers

    def addNum(self, num: int) -> None:
        # we want to take the minimum of max heap
        # we want to take the maximum of min heap
        median = self.findMedian()
        if num <= median:
            heapq.heappush_max(self._max_heap, num)
        else:
            heapq.heappush(self._min_heap, num)
        min_size = len(self._min_heap)
        max_size = len(self._max_heap)
        # we need to make sure that they have almost equal size
        if abs(max_size - min_size) > 1:
            if max_size > min_size:
                num_move = heapq.heappop_max(self._max_heap)
                heapq.heappush(self._min_heap, num_move)
            else:
                num_move = heapq.heappop(self._min_heap)
                heapq.heappush_max(self._max_heap, num_move)
        

    def findMedian(self) -> float:
        if not self._min_heap and not self._max_heap:
            return float("inf")
        min_size = len(self._min_heap)
        max_size = len(self._max_heap)
        if max_size == min_size:
            max_num = self._max_heap[0]
            min_num = self._min_heap[0]
            return (max_num + min_num) / 2.0
        elif max_size > min_size:
            max_num = self._max_heap[0]
            return max_num
        else:
            min_num = self._min_heap[0]
            return min_num
