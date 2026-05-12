import heapq

class MedianFinder:

    def __init__(self):
        # lower: smaller half, max-heap
        # upper: larger half, min-heap
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        # Decide where num belongs.
        # Question: if upper exists and num is bigger than upper[0],
        # should num go to lower or upper?
        if self.upper and num > self.upper[0]:
            heapq.heappush(self.upper, num)
        else:
            heapq.heappush_max(self.lower, num)

        # Rebalance sizes.
        # Invariant: abs(len(lower) - len(upper)) <= 1
        if len(self.upper) - len(self.lower) > 1:
            moved = heapq.heappop(self.upper)
            heapq.heappush_max(self.lower, moved)

        elif len(self.lower) - len(self.upper) > 1:
            moved = heapq.heappop_max(self.lower)
            heapq.heappush(self.upper, moved)

    def findMedian(self) -> float:
        # LeetCode says findMedian is only called after at least one addNum.
        if not  self.lower and not self.upper:
            return 0
        # If lower has more elements, median is max(lower).
        if len(self.lower) > len(self.upper):
            return self.lower[0]
        # If upper has more elements, median is min(upper).
        if len(self.lower) < len(self.upper):
            return self.upper[0]

        # Equal sizes: average max(lower) and min(upper).
        return (self.upper[0] + self.lower[0]) / 2