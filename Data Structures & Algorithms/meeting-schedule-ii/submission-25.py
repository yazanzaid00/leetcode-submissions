import heapq
from typing import List

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List["Interval"]) -> int:
        # Edge case: no meetings => no rooms.
        if not intervals:
            return 0

        # 1) Sort by start time so we process meetings in chronological order.
        intervals.sort(key=lambda it: (it.start, it.end))

        # Heap stores end times of ongoing meetings (rooms in use).
        min_heap: List[int] = []

        max_rooms = 0
        # 2) Process each meeting
        for it in intervals:
            # TODO: if a room is free, reuse it
            while min_heap and min_heap[0] <= it.start:
                heapq.heappop(min_heap)
            
            # consume next it
            heapq.heappush(min_heap, it.end)
            max_rooms = max(max_rooms, len(min_heap))
            

        # 3) Because heap size never decreases in this one-pop-per-interval formulation,
        # final heap length equals max rooms needed.
        return max_rooms
